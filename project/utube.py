'''
from pytube import YouTube


link = input("Enter the YouTube video URL: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()

destination = "D:\MOVIES\Youtube\Videos"

video.download(output_path= destination)
print(yt.title + " Download is completed successfully")'''

from pytube import YouTube

def download_youtube_video(link, destination):
  yt = YouTube(link)

  video = yt.streams.get_highest_resolution()

  video.download(output_path=destination)

  return yt.title


if __name__ == "__main__":
  link = input("Enter the YouTube video URL: ")
  destination = "D:\MOVIES\Youtube\Videos"

  title = download_youtube_video(link, destination)

  print(title + " Download is completed successfully")

