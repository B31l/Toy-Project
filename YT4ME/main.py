from pytube import YouTube
from datetime import datetime
import eel
import os

import eyed3
# import pygame

WIDTH = 1000
HEIGHT = 600
PATH = './download/'

"""
<Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">   
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">  
<Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">       
<Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">       
<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio"> 
"""
    

def print_stream(lst):
    """ 공유 링크의 stream을 출력 """
    for i in lst:
        print(i)


@eel.expose
def download_mp3(SHARE_LINK):
    yt = YouTube(SHARE_LINK)
    stream_audio = yt.streams.get_by_itag(251)  # 비트전송률 160kbps
    # yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download(PATH, f'{yt.title}.mp3')
    try:
        file_name = f"{yt.title}.mp3"
        stream_audio.download(PATH, file_name)
    except:
        d = datetime.now()
        file_name = f"{d.year}-{d.month:02d}-{d.day:02d}-{d.hour:02d}{d.minute:02d}{d.second:02d}.mp3"
        stream_audio.download(PATH, file_name)
    return yt.title


@eel.expose
def recent_mp3():
    EXT = "mp3"
    recent_list = []
    [recent_list.append(x) for x in os.listdir(PATH) if x.endswith(EXT)]
    return recent_list


eel.init("web")
eel.start("index.html", size=(WIDTH + 16, HEIGHT + 39))