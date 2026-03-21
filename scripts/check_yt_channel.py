"""
check_yt_channel.py

Monitors a YouTube channel for new videos using the public RSS feed
(no API key required). Appends new entries to a ytlinks .txt file
in the format used by this project:

  <index> <title> <url> <date>

Usage:
  python scripts/check_yt_channel.py

Configuration is done via the CHANNELS list below.
"""

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration — add / remove channels here
# ---------------------------------------------------------------------------
CHANNELS = [
    {
        "name": "ThalawathugodaB series",
        "channel_id": "UC63kf7W9KLLCj0jK6HF5PdA",
        # Only videos whose title contains this phrase will be added.
        # Set to None to accept all videos from the channel.
        "filter_phrase": "තලවතුගොඩ",
        "ytlinks_file": "NivanMagaUdesaDesana/ThalawathugodaB/ThalawathugodaB_ytlinks.txt",
    },
    {
        "name": "Kaluthara L series",
        "channel_id": "UC63kf7W9KLLCj0jK6HF5PdA",
        # Only videos whose title contains this phrase will be added.
        # Set to None to accept all videos from the channel.
        "filter_phrase": "Kalutara Bodhiya L",
        "ytlinks_file": "KalutaraBodhiya/L_series/L_series_ytlinks.txt",
    },
    {
        "name": "Maharagama A series",
        "channel_id": "UC63kf7W9KLLCj0jK6HF5PdA",
        # Only videos whose title contains this phrase will be added.
        # Set to None to accept all videos from the channel.
        "filter_phrase": "මහරගම",
        "ytlinks_file": "NivanMagaUdesaDesana\MaharagamaA\MaharagamaA_ytlinks.txt",
    },
    {
        "name": "Abhidharma Aruth D series",
        "channel_id": "UCHB486800OSZYo-umwIo72w",
        # Only videos whose title contains this phrase will be added.
        # Set to None to accept all videos from the channel.
        "filter_phrase": "පොල්ගස්ඔවිට",
        "ytlinks_file": "AbhidharmaAruth\D_series\AbhidharmaAruth_D_ytlinks.txt",
    },
    # Add more channels as needed:
    # {
    #     "name": "KalutaraBodhiya L series",
    #     "channel_id": "REPLACE_WITH_CHANNEL_ID",
    #     "filter_phrase": None,
    #     "ytlinks_file": "KalutaraBodhiya/L_series/L_series_ytlinks.txt",
    # },
]

RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
YT_NS   = "http://www.w3.org/2005/Atom"

# ---------------------------------------------------------------------------

def fetch_rss(channel_id: str) -> list[dict]:
    """Return a list of {video_id, title, published} dicts from the RSS feed."""
    url = RSS_URL.format(channel_id=channel_id)
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = resp.read()
    except Exception as exc:
        print(f"  ERROR fetching RSS: {exc}", file=sys.stderr)
        return []

    root = ET.fromstring(data)
    videos = []
    for entry in root.findall(f"{{{YT_NS}}}entry"):
        video_id_el = entry.find("{http://www.youtube.com/xml/schemas/2015}videoId")
        title_el    = entry.find(f"{{{YT_NS}}}title")
        pub_el      = entry.find(f"{{{YT_NS}}}published")

        if video_id_el is None or title_el is None or pub_el is None:
            continue

        pub_date = datetime.fromisoformat(pub_el.text.replace("Z", "+00:00"))
        videos.append({
            "video_id":  video_id_el.text.strip(),
            "title":     title_el.text.strip(),
            "published": pub_date,
        })
    return videos


def load_known_ids(ytlinks_file: Path) -> set[str]:
    """Return the set of YouTube video IDs already present in the file."""
    if not ytlinks_file.exists():
        return set()
    ids = set()
    for line in ytlinks_file.read_text(encoding="utf-8").splitlines():
        match = re.search(r"youtube\.com/watch\?v=([\w-]+)", line)
        if match:
            ids.add(match.group(1))
    return ids


def last_index(ytlinks_file: Path) -> int:
    """Return the highest numeric index found in the file (0 if empty)."""
    if not ytlinks_file.exists():
        return 0
    max_idx = 0
    for line in ytlinks_file.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*(\d+)\s", line)
        if m:
            max_idx = max(max_idx, int(m.group(1)))
    return max_idx


def format_date(dt: datetime) -> str:
    """Format a datetime as YYYY-Mon-DD (e.g. 2026-Mar-21)."""
    return dt.strftime("%Y-%b-%d")


def process_channel(cfg: dict) -> bool:
    """Check one channel and append new videos. Returns True if anything was added."""
    name          = cfg["name"]
    channel_id    = cfg["channel_id"]
    filter_phrase = cfg.get("filter_phrase")
    ytlinks_file  = Path(cfg["ytlinks_file"])

    print(f"\n[{name}]")

    if not channel_id or channel_id.startswith("REPLACE_"):
        print("  Skipping — channel_id not configured.")
        return False

    videos = fetch_rss(channel_id)
    if not videos:
        print("  No videos returned from RSS feed.")
        return False

    # Apply optional title filter
    if filter_phrase:
        videos = [v for v in videos if filter_phrase in v["title"]]
        print(f"  Filter '{filter_phrase}': {len(videos)} matching video(s) in feed.")

    known_ids  = load_known_ids(ytlinks_file)
    new_videos = [v for v in videos if v["video_id"] not in known_ids]

    if not new_videos:
        print("  No new videos found.")
        return False

    # Sort oldest-first so indices stay in chronological order
    new_videos.sort(key=lambda v: v["published"])

    idx = last_index(ytlinks_file)
    lines_to_append = []
    for video in new_videos:
        idx += 1
        url  = f"https://www.youtube.com/watch?v={video['video_id']}"
        date = format_date(video["published"])
        line = f"{idx} {video['title']} {url} {date}"
        lines_to_append.append(line)
        print(f"  + [{idx}] {video['title']}  ({date})")

    # Ensure file ends with a newline before appending
    existing = ytlinks_file.read_text(encoding="utf-8") if ytlinks_file.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    ytlinks_file.write_text(
        existing + "\n".join(lines_to_append) + "\n",
        encoding="utf-8"
    )
    print(f"  Appended {len(lines_to_append)} new entry/entries to {ytlinks_file}")
    return True


def main():
    for cfg in CHANNELS:
        process_channel(cfg)
    sys.exit(0)


if __name__ == "__main__":
    main()
