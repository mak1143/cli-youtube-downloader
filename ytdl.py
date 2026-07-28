#!/usr/bin/env python3
"""ytdl --> cli youtube downloader"""

import argparse
import os
import re
import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import RegexMatchError, VideoUnavailable


def download_video(url=None, output=None):
    if not url:
        url = input("Enter YouTube URL: ").strip()
    if not url:
        print("No URL provided.")
        return

    if not re.match(r"https?://(music\.)?(youtube\.com|youtu\.be)/", url):
        print("Invalid URL — must be a YouTube URL (youtube.com or youtu.be)")
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except (RegexMatchError, VideoUnavailable) as e:
        print(f"Invalid or unavailable video: {e}")
        return

    try:
        stream = yt.streams.get_highest_resolution()

        dst = output or os.path.expanduser("~/Downloads/")
        path = stream.download(output_path=dst)
        print(f"Downloaded: {yt.title} -> {path}")

    except KeyboardInterrupt:
        sys.exit()


# adding safe guide
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos")
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument("-o", "--output", default=None, help="Output directory")
    args = parser.parse_args()
    download_video(args.url, args.output)
