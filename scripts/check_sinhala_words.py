import argparse
import os
import re
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Root directory of the repository (one level up from scripts/)
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Default folders to scan (relative paths from the repository root)
DEFAULT_FOLDERS = [
    "current/HomagamaA/docs",
    "current/KalutaraBodhiyaM/docs",
]

# Patterns to search for and their corresponding replacements
PATTERNS = {
    "කලාත්රයේම": "කාලාත්රයේම",
    "කලාත්‍රයේම": "කාලාත්‍රයේම",
    "කලත්‍රයේම": "කාලාත්‍රයේම",
    "බබය": "බඹය",
    "මුල": "මූල",
    "මුලික": "මූලික",
    "සදහා":"සඳහා",
    "අනාත්මිය": "අනාත්මීය",
    "පිලිබද": "පිළිබඳ",
    "හදුනා":  "හඳුනා",
    "හදුන්වනු": "හඳුන්වනු",
    "හදුන්වන්නේ":  "හඳුන්වන්නේ",
    "හදුන්වයි": "හඳුන්වයි",
    "සමුහ": "සමූහ",
    "ද්වේග": "ද්වේශ",
    " හුමින් ":" භූමින් ",
}

# Patterns that should only match as a complete Sinhala word
# (prevents "මුල" from matching inside valid words like "මුල්" or "මුලින්",
# or overlapping with "මුලික")
WHOLE_WORD_PATTERNS = {
    "මුල",
}

REPORT_FILENAME = "possible_correctios.txt"

# Regex character class for Sinhala characters + Zero-Width Joiner (ZWJ)
SINHALA_CHAR_CLASS = r"[\u0d80-\u0dff\u200d]"
SINHALA_WORD_RE = re.compile(f"{SINHALA_CHAR_CLASS}+")


def build_pattern_regex(pattern: str, whole_word: bool = False) -> re.Pattern:
    """
    Build a regex for a Sinhala pattern that also tolerates an optional
    Zero-Width Joiner (U+200D) after al-lakuna (U+0DCA), e.g., matching both
    'කලාත්රයේම' and 'කලාත්‍රයේම'.
    """
    # Normalize by stripping existing ZWJ after al-lakuna, then make ZWJ optional
    normalized = pattern.replace("\u0dca\u200d", "\u0dca")
    parts = [re.escape(part) for part in normalized.split("\u0dca")]
    regex_str = "\u0dca\u200d?".join(parts)

    if whole_word:
        regex_str = f"(?<!{SINHALA_CHAR_CLASS}){regex_str}(?!{SINHALA_CHAR_CLASS})"

    return re.compile(regex_str)


def compute_replacement(matched_text: str, raw_pattern: str, raw_replacement: str) -> str:
    """
    Preserve Zero-Width Joiner (U+200D) in the replacement if it was present
    in the matched text from the HTML file.
    """
    if "\u0dca\u200d" in matched_text and "\u0dca\u200d" not in raw_replacement:
        return raw_replacement.replace("\u0dca", "\u0dca\u200d")
    return raw_replacement


def find_enclosing_word(line: str, start: int, end: int) -> tuple[str, int, int]:
    """
    Find the full Sinhala word enclosing the character span [start, end).
    Returns (full_word, word_start, word_end).
    """
    for match in SINHALA_WORD_RE.finditer(line):
        if match.start() <= start and match.end() >= end:
            return match.group(0), match.start(), match.end()
    return line[start:end], start, end


def build_context_snippet(line: str, word_start: int, word_end: int, window: int = 35) -> str:
    """
    Create a single-line context snippet highlighting the enclosing word in brackets.
    """
    prefix_start = max(0, word_start - window)
    suffix_end = min(len(line), word_end + window)

    prefix = line[prefix_start:word_start]
    word = line[word_start:word_end]
    suffix = line[word_end:suffix_end]

    if prefix_start > 0:
        prefix = "..." + prefix.lstrip()
    else:
        prefix = prefix.lstrip()

    if suffix_end < len(line):
        suffix = suffix.rstrip() + "..."
    else:
        suffix = suffix.rstrip()

    snippet = f"{prefix}[{word}]{suffix}"
    # Collapse any internal tabs/newlines so the report format stays clean
    return re.sub(r"\s+", " ", snippet).strip()


def scan_file(filepath: str, compiled_patterns: list[tuple[str, str, re.Pattern]]) -> list[dict]:
    """
    Scan a single HTML file and return a list of match dictionaries sorted by (line, col).
    """
    matches = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_idx, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\r\n")
        line_matches = []

        for raw_pat, raw_rep, regex in compiled_patterns:
            for m in regex.finditer(line):
                start, end = m.start(), m.end()
                matched_text = m.group(0)
                replacement_text = compute_replacement(matched_text, raw_pat, raw_rep)

                full_word, w_start, w_end = find_enclosing_word(line, start, end)
                replaced_word = (
                    full_word[: start - w_start]
                    + replacement_text
                    + full_word[end - w_start :]
                )
                context = build_context_snippet(line, w_start, w_end)

                line_matches.append(
                    {
                        "line": line_idx,
                        "col": start + 1,  # 1-based column
                        "end_col": end + 1,
                        "pattern": raw_pat,
                        "matched_text": matched_text,
                        "replacement_text": replacement_text,
                        "full_word": full_word,
                        "replaced_word": replaced_word,
                        "context": context,
                    }
                )

        # Sort matches on the same line by column position
        line_matches.sort(key=lambda x: (x["col"], -(x["end_col"] - x["col"])))

        # Filter out any overlapping matches on the same line (longest/first wins)
        non_overlapping = []
        last_end = -1
        for item in line_matches:
            if item["col"] >= last_end:
                non_overlapping.append(item)
                last_end = item["end_col"]

        matches.extend(non_overlapping)

    return matches


def scan_folder(folder_rel_path: str, compiled_patterns: list[tuple[str, str, re.Pattern]]) -> None:
    """
    Scan all HTML files in the given folder (relative to REPO_ROOT) and write
    possible_correctios.txt inside that folder.
    """
    folder_abs_path = os.path.normpath(os.path.join(REPO_ROOT, folder_rel_path))
    if not os.path.isdir(folder_abs_path):
        print(f"[WARNING] Folder not found: {folder_rel_path} ({folder_abs_path})")
        return

    html_files = sorted(
        f
        for f in os.listdir(folder_abs_path)
        if f.lower().endswith(".html") and os.path.isfile(os.path.join(folder_abs_path, f))
    )

    print(f"\nScanning folder: {folder_rel_path} ({len(html_files)} HTML files)")

    all_results = []
    files_with_matches = 0

    for filename in html_files:
        filepath = os.path.join(folder_abs_path, filename)
        file_matches = scan_file(filepath, compiled_patterns)
        if file_matches:
            files_with_matches += 1
            for item in file_matches:
                item["file"] = filename
                all_results.append(item)

    report_path = os.path.join(folder_abs_path, REPORT_FILENAME)
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(
            "# ==============================================================================\n"
            "# Possible Sinhala Word Corrections Report\n"
            f"# Folder: {folder_rel_path}\n"
            f"# Total HTML files scanned: {len(html_files)}\n"
            f"# Files with matches: {files_with_matches}\n"
            f"# Total matches found: {len(all_results)}\n"
            "#\n"
            "# Instructions:\n"
            "#   1. Review the matches listed below.\n"
            "#   2. Delete or comment out (add '#' at the start of the line) any item\n"
            "#      that you DO NOT want replaced.\n"
            "#   3. Run `python scripts/replace_sinhala_words.py` to apply the approved\n"
            "#      replacements.\n"
            "#\n"
            "# Columns:\n"
            "#   FILE | LINE:COL | MATCH -> REPLACEMENT | WORD_PREVIEW | CONTEXT\n"
            "# ==============================================================================\n\n"
        )

        if not all_results:
            report_file.write("# No matching patterns found in any HTML files.\n")
        else:
            current_file = None
            for item in all_results:
                if item["file"] != current_file:
                    if current_file is not None:
                        report_file.write("\n")
                    current_file = item["file"]
                    report_file.write(f"# --- File: {current_file} ---\n")

                line_col = f"{item['line']}:{item['col']}"
                match_rep = f"{item['matched_text']} -> {item['replacement_text']}"
                word_preview = f"({item['full_word']} -> {item['replaced_word']})"
                report_file.write(
                    f"{item['file']} | {line_col} | {match_rep} | {word_preview} | {item['context']}\n"
                )

    print(f"  -> Found {len(all_results)} matches across {files_with_matches} files.")
    print(f"  -> Report written to: {os.path.relpath(report_path, REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scan HTML files in one or more folders for Sinhala words/patterns and generate possible_correctios.txt."
    )
    parser.add_argument(
        "folders",
        nargs="*",
        default=DEFAULT_FOLDERS,
        help="Relative folder paths from the repository root (default: %(default)s)",
    )
    args = parser.parse_args()

    compiled_patterns = [
        (pat, rep, build_pattern_regex(pat, whole_word=(pat in WHOLE_WORD_PATTERNS)))
        for pat, rep in PATTERNS.items()
    ]

    for folder in args.folders:
        scan_folder(folder, compiled_patterns)


if __name__ == "__main__":
    main()
