from pytubefix import YouTube
from pytubefix.cli import on_progress


# def download_video(inputUrl, yt , ys ,dst):
#     inputUrl = input("please enter youtube url>: ")
#     yt = YouTube(url, on_progress_callback=on_progress)
#
#     ys = yt.streams.get_highest_resolution()
#
#     dst = output("home/shoyo/Downloads")
#     ys.download(dst)
#     print(f"Completed! file saved to: {dst}")
#
#
# download_video(inputUrl,yt,ys,dst)
#
def download_video():
    inputUrl = input("please enter youtube url>: ")
    yt = YouTube(url, on_progress_callback=on_progress)

    ys = yt.streams.get_highest_resolution()

    dst = output("home/shoyo/Downloads")
    ys.download(dst)
    print(f"Completed! file saved to: {dst}")


download_video()
