# 좌표 최적화를 위해 스크린샷을 찍습니다.
import pyautogui
import time
import os
from datetime import datetime

file_name = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
if not os.path.isdir("test_screenshot"):
    os.mkdir("./test_screenshot")
time.sleep(3)
pyautogui.screenshot(f"./test_screenshot/{file_name}.png")