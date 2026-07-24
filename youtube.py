import os
import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video():
    try:
        print("Please use youtube music for audio")
        inputUrl = input("please enter youtube url>: ")
        yt = YouTube(inputUrl, on_progress_callback=on_progress)

        ys = yt.streams.get_highest_resolution()

        dst = os.path.expanduser("~/Downloads/")
        ys.download(output_path=dst)
        print(f"Completed! {yt.title} >: file saved to: {dst}")

    except KeyboardInterrupt:
        sys.exit()


download_video()
