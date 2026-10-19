import argparse
from collections import defaultdict
import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Root directory of the repository (one level up from scripts/)
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Default folders to process (relative paths from the repository root)
DEFAULT_FOLDERS = [
    "current/HomagamaA/docs",
    "current/KalutaraBodhiyaM/docs",
]

REPORT_FILENAME = "possible_correctios.txt"


def parse_report_file(report_path: str) -> list[dict]:
    """
    Parse possible_correctios.txt and return a list of approved replacement entries.
    Lines starting with '#' or empty lines are ignored.
    """
    entries = []
    with open(report_path, "r", encoding="utf-8") as f:
        for report_line_num, raw_line in enumerate(f, start=1):
            stripped = raw_line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            parts = [p.strip() for p in stripped.split("|")]
            if len(parts) < 3:
                print(
                    f"  [WARNING] Skipping malformed line {report_line_num} in {report_path}: {stripped}"
                )
                continue

            filename = parts[0]
            line_col_str = parts[1]
            match_rep_str = parts[2]
            word_preview = parts[3] if len(parts) > 3 else ""
            context = " | ".join(parts[4:]) if len(parts) > 4 else ""

            try:
                line_str, col_str = line_col_str.split(":")
                line_num = int(line_str.strip())
                col_num = int(col_str.strip())
            except ValueError:
                print(
                    f"  [WARNING] Invalid LINE:COL '{line_col_str}' on line {report_line_num} in {report_path}"
                )
                continue

            if "->" not in match_rep_str:
                print(
                    f"  [WARNING] Invalid MATCH -> REPLACEMENT '{match_rep_str}' on line {report_line_num} in {report_path}"
                )
                continue

            matched_text, replacement_text = [
                s.strip() for s in match_rep_str.split("->", 1)
            ]

            entries.append(
                {
                    "report_line": report_line_num,
                    "file": filename,
                    "line": line_num,
                    "col": col_num,
                    "matched_text": matched_text,
                    "replacement_text": replacement_text,
                    "word_preview": word_preview,
                    "context": context,
                }
            )

    return entries


def process_folder(
    folder_rel_path: str, dry_run: bool = False, interactive: bool = False
) -> None:
    """
    Read possible_correctios.txt in folder_rel_path and apply the selected replacements.
    """
    folder_abs_path = os.path.normpath(os.path.join(REPO_ROOT, folder_rel_path))
    report_path = os.path.join(folder_abs_path, REPORT_FILENAME)

    if not os.path.isfile(report_path):
        print(
            f"[WARNING] Report file not found: {os.path.relpath(report_path, REPO_ROOT)}"
        )
        print("          Run `python scripts/check_sinhala_words.py` first.")
        return

    entries = parse_report_file(report_path)
    print(
        f"\nProcessing folder: {folder_rel_path} ({len(entries)} approved entries in {REPORT_FILENAME})"
    )

    if not entries:
        print("  -> No active replacement entries found.")
        return

    # Group entries by filename
    entries_by_file: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        entries_by_file[entry["file"]].append(entry)

    total_applied = 0
    total_skipped = 0
    files_modified = 0

    for filename, file_entries in entries_by_file.items():
        filepath = os.path.join(folder_abs_path, filename)
        if not os.path.isfile(filepath):
            print(f"  [WARNING] Target HTML file not found: {filename}")
            total_skipped += len(file_entries)
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Group by line number and sort descending by column so replacements
        # on the same line do not shift earlier column positions.
        entries_by_line: dict[int, list[dict]] = defaultdict(list)
        for entry in file_entries:
            entries_by_line[entry["line"]].append(entry)

        file_changes = 0

        for line_num in sorted(entries_by_line.keys()):
            if line_num < 1 or line_num > len(lines):
                print(
                    f"  [WARNING] {filename}:{line_num} is out of range (file has {len(lines)} lines)."
                )
                total_skipped += len(entries_by_line[line_num])
                continue

            line_content = lines[line_num - 1]
            # Sort in reverse column order (right-to-left)
            line_items = sorted(
                entries_by_line[line_num], key=lambda x: x["col"], reverse=True
            )

            for item in line_items:
                col_idx = item["col"] - 1
                target = item["matched_text"]
                replacement = item["replacement_text"]
                actual_slice = line_content[col_idx : col_idx + len(target)]

                if actual_slice != target:
                    print(
                        f"  [SKIP] {filename}:{line_num}:{item['col']} - expected '{target}', "
                        f"found '{actual_slice}' (file may have already been updated or modified)."
                    )
                    total_skipped += 1
                    continue

                if interactive:
                    print(
                        f"\n{filename} [Line {line_num}, Col {item['col']}] "
                        f"{target} -> {replacement} {item['word_preview']}"
                    )
                    if item["context"]:
                        print(f"  Context: {item['context']}")
                    ans = input("  Replace this occurrence? [y/N/q]: ").strip().lower()
                    if ans == "q":
                        print("Aborted by user.")
                        return
                    if ans != "y":
                        total_skipped += 1
                        continue

                # Apply replacement at exact slice
                line_content = (
                    line_content[:col_idx]
                    + replacement
                    + line_content[col_idx + len(target) :]
                )
                file_changes += 1
                total_applied += 1

            lines[line_num - 1] = line_content

        if file_changes > 0:
            files_modified += 1
            if dry_run:
                print(f"  [DRY-RUN] Would update {file_changes} occurrence(s) in {filename}")
            else:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print(f"  [UPDATED] Replaced {file_changes} occurrence(s) in {filename}")

    mode_label = " (DRY-RUN)" if dry_run else ""
    print(
        f"\nSummary for {folder_rel_path}{mode_label}: "
        f"{total_applied} replaced across {files_modified} file(s), {total_skipped} skipped."
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply selected Sinhala word replacements from possible_correctios.txt."
    )
    parser.add_argument(
        "folders",
        nargs="*",
        default=DEFAULT_FOLDERS,
        help="Relative folder paths from the repository root (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview replacements without modifying any HTML files.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Ask for confirmation (y/n) before each replacement.",
    )
    args = parser.parse_args()

    for folder in args.folders:
        process_folder(folder, dry_run=args.dry_run, interactive=args.interactive)


if __name__ == "__main__":
    main()
