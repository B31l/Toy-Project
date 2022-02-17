from PIL import ImageGrab, ImageChops, ImageStat
import pyautogui
import time
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)
rate = engine.getProperty('rate')
engine.setProperty('volume', 1) # 0~1 
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

def locations_to_tuple(x1, y1, x2, y2):
    x = x1 + 1
    y = y1 + 1
    width = x2 - x1 - 1
    height = y2 - y1 - 1
    return (x, y, width, height)


BOOK_NAME = input("책 이름을 입력하세요: ")
if not os.path.isdir(BOOK_NAME):
    os.mkdir(f"./{BOOK_NAME}")
x1 = int(input("좌측 상단 외곽의 x좌표를 입력하세요: "))
y1 = int(input("좌측 상단 외곽의 y좌표를 입력하세요: "))
x2 = int(input("우측 하단 외곽의 x좌표를 입력하세요: "))
y2 = int(input("우측 하단 외곽의 y좌표를 입력하세요: "))
BOOK_SIZE = locations_to_tuple(x1, y1, x2, y2)
mode = input("")

if not os.path.isdir("locations"):
    os.mkdir(f"./locations")
with open(f"./locations/{BOOK_NAME}.txt", "w", encoding="utf-8") as f:
    f.write(f"{BOOK_NAME}: {BOOK_SIZE}")


print("곧 캡처를 시작합니다...")
time.sleep(5)
engine.say("시작하세요") 
engine.runAndWait()
engine.stop()





# 양면 인쇄
# im1 = ImageGrab.grab()
# pyautogui.screenshot(f"./{BOOK_NAME}/1 - 2.png", region=BOOK_SIZE)
# count = 3
# while True:
#     im2 = ImageGrab.grab()
#     im = ImageChops.difference(im1, im2)
#     stat = ImageStat.Stat(im)
#     if stat.sum != [0, 0, 0]:
#         file_name = f"./{BOOK_NAME}/{count} - {count + 1}.png"
#         pyautogui.screenshot(file_name, region=BOOK_SIZE)
#         count += 2
#         im1 = im2

# 단면 인쇄
im1 = ImageGrab.grab()
pyautogui.screenshot(f"./{BOOK_NAME}/0001.png", region=BOOK_SIZE)
count = 2
while True:
    im2 = ImageGrab.grab()
    im = ImageChops.difference(im1, im2)
    stat = ImageStat.Stat(im)
    if stat.sum != [0, 0, 0]:
        file_name = f"./{BOOK_NAME}/{count:04d}.png"
        pyautogui.screenshot(file_name, region=BOOK_SIZE)
        count += 1
        im1 = im2