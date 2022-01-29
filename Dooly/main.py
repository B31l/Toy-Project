import click
import pyautogui


def check_by_image(img_name):
    try:
        p_list = pyautogui.locateAllOnScreen(f"./img/{img_name}.png")   # Box 객체
        p_list = list(p_list)
        return p_list[0]
    except:
        return None


def click_by_image(img_name):
    target = check_by_image(img_name)
    if target:
        p_center = pyautogui.center(target)
        pyautogui.click(p_center)


def click_by_location(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


if __name__ == "__main__":
    while True:
        # 현상수배 시작
        if check_by_image("check-1"):
            click_by_image("act-1-1")   # 클릭: 현상수배
            click_by_image("act-1-2")   # 클릭: 선택

        # 파티 선택
        elif check_by_image("check-2"):
            click_by_image("act-2-1")   # 클릭: 파티
            click_by_image("act-2-2")   # 클릭: 선택
            click_by_image("act-2-3")   # 클릭: 확정

        # 보물 선택
        elif check_by_image("check-5"):
            click_by_location(800, 500)
            click_by_location(1150, 850)
            # click_by_image("act-5-1")

        # 맵
        elif check_by_image("check-3"):
            click_by_image("act-3-1")   # 클릭: 시작
            # 모든 블록에 대해 검사
            for i in range(4):
                click_by_location(500 + (200 * i), 500)
                click_by_image("act-3-1")   # 클릭: 시작
                click_by_image("act-3-2")   # 클릭: 드러내기
                click_by_image("act-3-3")   # 클릭: 집기
                click_by_image("act-3-4")   # 클릭: 방문
                click_by_image("act-3-5")   # 클릭: 공간이동

        # 전투 준비  
        elif check_by_image("gameBtn_ready"):
            click_by_image("gameBtn_ready")

        # 전투 시작
        elif check_by_image("gameBtn_start") or check_by_image("gameBtn_start_alone"):
            click_by_image("act-4-1")
            click_by_location(1400, 1200)
            click_by_image("gameBtn_start")
            click_by_image("gameBtn_start_alone")



        # 현상수배 종료
        elif check_by_image("check-6"):
            click_by_image("act-6-1")

        else:
            click_by_location(800, 500)
            pyautogui.write("12345", interval=0.25)
            click_by_image("rewardBtn")