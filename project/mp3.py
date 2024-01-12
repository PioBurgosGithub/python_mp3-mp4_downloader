#import packages
from pytube import YouTube
import os 

#url input
yt = YouTube(input("Enter the URL of the video you want to download: "))

#extract audio only
video = yt.streams.filter(only_audio=True).first()

#path to download the audio
destination = "D:\MOVIES\Youtube\Audio"

#download the file
out_file = video.download(output_path= destination)

#save file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#result of success
print(yt.title + "Download is completed successfully")