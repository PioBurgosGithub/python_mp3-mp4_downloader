import os
from pytube import YouTube

def download_youtube_video(link, destination, audio_only=False):
  """Downloads a YouTube video to the specified destination directory.

  Args:
    link: The YouTube video URL.
    destination: The destination directory.
    audio_only: Whether to download the audio only.

  Returns:
    The title of the downloaded video.
  """

  yt = YouTube(link)

  if audio_only:
    video = yt.streams.filter(only_audio=True).first()
  else:
    video = yt.streams.get_highest_resolution()

  out_file = video.download(output_path=destination)

  if audio_only:
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

  return yt.title


def main():
  while True:
    print("Select what you want to download:")
    print("1. Video")
    print("2. Audio")
    print("3. Quit")
    x = input("Enter your choice: ")

    if x == "1":
      link = input("Enter the YouTube video URL: ")
      destination = "D:\MOVIES\Youtube\Videos"
      title = download_youtube_video(link, destination)
      print(title + " Download is completed successfully")

    elif x == "2":
      link = input("Enter the YouTube video URL: ")
      destination = "D:\MOVIES\Youtube\Audio"
      title = download_youtube_video(link, destination, audio_only=True)
      print(title + " Download is completed successfully")

    elif x == "3":
      print("Program Ended. Thank You for using Me")
      break

    else:
      print("Please enter a valid choice.")

    continue_downloading = input("Do you want to download again? yes/no > ")
    while continue_downloading.lower() not in ("yes", "no"):
      continue_downloading = input("Do you want to download again? yes/no > ")

    if continue_downloading == "no":
      break


if __name__ == "__main__":
  main()
