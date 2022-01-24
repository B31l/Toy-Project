import random, time # random, time import
PATH = "C:/WorkSpace/__ShowVoca/"  # 불러오는 파일 위치
MENU = ["학습", "OX 퀴즈", "스피드 퀴즈", "단어장", "검색"] # 메뉴리스트
CHAP = 15 # 총단원수

def menu_main(menu):        # 메인 메뉴 함수
    time.sleep(DELAY_MENU)  # 메뉴 로딩 시간
    #  __   _____   ___   _   
    #  \ \ / / _ \ / __| /_\  
    #   \ V / (_) | (__ / _ \ 
    #    \_/ \___/ \___/_/ \_\
    # http://patorjk.com/software/taag/#p=display&f=Small&t=VOCA
    print(" __   _____   ___   _   ".center(40)) # center: 중앙정렬
    print(" \\ \\ / / _ \\ / __| /_\\  ".center(40))
    print("  \\ V / (_) | (__ / _ \\ ".center(40))
    print("   \\_/ \\___/ \\___/_/ \\_\\".center(40))

    # 메뉴 인터페이스 구현
    print("-" * 40)
    print("♥ MENU ♥".center(40))
    for i in range(len(menu)):
        print("-" * 40)
        print(f"{i+1} : {menu[i]}")
    print("-" * 40)
    number = int(input("  : "))
    if   number == 1: menu_voca(1)   
    elif number == 2: menu_voca(2)
    elif number == 3: menu_voca(3)
    elif number == 4: func_mark()
    elif number == 5: func_search()

def menu_voca(number):
    idx = 1
    while True:
        print("-" * 40)
        for i in range(3):
            print(f"| Chapter {str(idx).zfill(2)}", end=" ") # zfill: 1 -> 01로표현
            idx += 1
        print("|", end="") # end : 줄바꿈없음
        print()
        if idx > CHAP:
            break
    print("-" * 40)
    if   number == 1: func_study()
    elif number == 2: func_ox()
    elif number == 3: func_speed()

def func_study():
    chap = int(input("챕터를 선택하세요 : "))
    something = voca_list[chap-1]
    ky = list(something.keys())
    random.shuffle(ky)  # suffle : 섞기
    print("모르면 z, 메뉴로 돌아가려면 n을 누르세요")
    moon = 0
    for i in ky:
        moon += 1
        print(f"{moon}. {i}", end=" ")
        answer = input()
        if answer == "z": marking(i)
        elif answer == "n": break
    menu_main(MENU)

def func_ox():
    chap = int(input("챕터를 선택하세요 : "))
    something = voca_list[chap-1]
    ky = list(something.keys())
    random.shuffle(ky)  # 섞어요 !
    print("메뉴로 돌아가려면 n을 누르세요")
    moon = 0
    rate = 0
    for i in ky:
        moon += 1
        print(f"{moon}. {i}")
        print()
        # 정답 생성
        perfect = something.get(i)
        example = ["", "", "", ""]
        n = random.randrange(4)
        example[n] = f"[{n+1}] {perfect}"
        # 오답 생성
        vl = list(something.values())
        random.shuffle(vl)
        dummy = []
        idx = -1
        while len(dummy) < 3:
            idx += 1
            if vl[idx] == perfect:
                continue
            else:
                dummy.append(vl[idx])
        # 리스트에 정답과 오답 넣기
        idx = 0
        for j in range(4):
            if example[j] != "": continue
            else: 
                example[j] = f"[{j+1}] {dummy[idx]}"
                idx += 1
        # 리스트 출력하기
        for j in range(4):
            print(example[j])
        print()
        # 입력받기
        answer = input()
        if answer == "n": break
        elif answer == "": 
            print("빈칸 -> 오답.")
            print()
            continue
        answer = int(answer)
        if answer == n+1: 
            print("정답입니다.")
            rate += 1
        else: print("오답입니다.")
        print()

    print(f"[ {rate} / {moon} ] 정답률 : {round(rate * 100 / moon, 2)} %") #round : 원하는자리
    menu_main(MENU)                                                           # 까지 반올림

def func_speed():
    print("░░░░░░░░░▄░░░░░░░░░░░░░░▄")
    print("░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌")
    print("░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐")
    print("░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐")
    print("░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐")
    print("░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌")
    print("░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌")
    print("░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐")
    print("░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌")
    print("░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌")
    print("▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐")
    print("▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌")
    print("▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐")
    print("░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌")
    print("░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐")
    print("░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌")
    print("░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀")
    print("░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀")
    print("░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀")
    print()
    print("준비 중 입니다....... 왈왈!!!")
    menu_main(MENU)

def func_mark(): # with A as B : 외부 파일 입출력
    with open(PATH + "mark.txt", "r", encoding="utf-8") as koko:
        kk = koko.readlines()
    mark_list = kk[1].split(" / ")[:-1]
    for i in range(len(mark_list)):
        o_my_girl = mark_list[i].split(" ")
        print(f"{o_my_girl[0].rjust(15)} : {o_my_girl[1]}") # rjust 오른쪽 정렬

    menu_main(MENU)
    
def func_search():
    print("단어 ㄱ")
    keyword = input("")
    for i in range(15):
        result = voca_list[i].get(keyword)
        if result != None:
            break
        else: continue
    print(result)
    menu_main(MENU)
    
def marking(ky): 
    for i in range(15):
        result = voca_list[i].get(ky) # get : 딕셔너리의 키를 리스트로 반환
        if result != None:
            break
        else: continue
    tt = f"{ky} {result} / "
    with open(PATH + "mark.txt", "a", encoding="utf-8") as kokoa: #encording : 한글로 입출력가능
        kokoa.write(tt) # a: 이어쓰기

# Voca
with open(PATH + "voca750.txt", "r", encoding="utf-8") as roro:
    rr = roro.readlines() # r: 읽기
rororong = []
for i in range(CHAP): 
    rororong.append(rr[i+1].split(" / "))
voca_list = []
for i in range(CHAP):
    ky = []
    vl = []
    for j in range(50): 
        nos = rororong[i][j].split(" ")
        ky.append(nos[0])
        vl.append(nos[1])
    voca_list.append(dict(zip(ky, vl)))

# Setting 
with open(PATH + "setting.txt", "r", encoding="utf-8") as dodo:
    dd = dodo.readlines()
DELAY_MENU = int(dd[1])
DELAY_QUIZ = int(dd[2])
# 처음메뉴구성을 마지막에 낭만스럽게 넣음
menu_main(MENU)