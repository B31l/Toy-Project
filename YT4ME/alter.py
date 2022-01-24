import eyed3
import os

PATH = './download/'
EXT = "mp3"
recent_list = []
[recent_list.append(x) for x in os.listdir(PATH) if x.endswith(EXT)]
print(recent_list)

for i in recent_list:

    audiofile = eyed3.load(i[:-4])
    audiofile.tag.artist = u"Integrity"
    audiofile.tag.album = u"Humanity Is The Devil"
    audiofile.tag.album_artist = u"Integrity"
    audiofile.tag.title = u"Hollow"
    audiofile.tag.track_num = 2

    audiofile.tag.save()
