from pytube import YouTube
from datetime import datetime

def print_stream(lst):
    for i in lst:
        print(i)

PATH = './download/'
SHARE_LINK = input("링크 입력: ")

yt = YouTube(SHARE_LINK)
stream_audio = yt.streams.get_by_itag(251)  # 비트전송률 160kbps

try:
    file_name = f"{yt.title}.mp3"
    stream_audio.download(PATH, file_name)
except:
    d = datetime.now()
    file_name = f"{d.year}-{d.month:02d}-{d.day:02d}-{d.hour:02d}{d.minute:02d}{d.second:02d}.mp3"
    stream_audio.download(PATH, file_name)