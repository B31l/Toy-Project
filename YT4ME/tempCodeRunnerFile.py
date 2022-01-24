def alter_mp3(file_name):
    current = eyed3.load(file_name)
    current.tag.artist = input("아티스트: ")
    current.tag.album = input("앨범: ")
    current.tag.title = input("타이틀: ")