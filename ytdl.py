#!/usr/bin/env python3
"""ytdl --> cli youtube downloader"""

import argparse
import os
import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video(url=None, output=None):
    try:
        if not url:
            url = input("Enter YouTube URL: ").strip()

        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()

        # destination of downloader file
        dst = output or os.path.expanduser("~/Downloads/")
        path = stream.download(output_path=dst)
        print(f"Downloaded: {yt.title} -> {path}")

        # exit program
    except KeyboardInterrupt:
        sys.exit()


# adding safe guide
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube vidoes")
    parser.add_argument("url", nargs="?", help="YouTube vidoe URL")
    parser.add_argument("-o", "--output", default=None, help="Output directory")
    args = parser.parse_args()
    download_video(args.url, args.output)
