# Pygame 라이브러리를 이용해 만든 게임 Shooter입니다.
# 이미지, 사운드 파일 경로를 확인해 주세요.
# 사운드 파일을 따로 준비해 주세요.

import pygame, random, sys
from pygame import *
# PATH = "C:/WorkSpace/Toy-Project/Shooter/"
PATH = "./"
WORKSPACE_IMAGE = PATH+'img/'
WORKSPACE_SOUND = PATH+'sound/'

WINDOWWIDTH, WINDOWHEIGHT = [600, 800]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# 플레이어의 속도
PLAYERSPEED = 8

# 적
BADDIEMINSIZE = 15
BADDIEMAXSIZE = 30
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
BADDIEADDCOUNT = 15
METEORSIZE = 100
METEORMINSPEED = 3
METEORMAXSPEED = 10
METEORADDCOUNT = 60

# 무기 타입
MISSILE = 0
BOMB = 1

def init():
    global mainClock, windowSurface
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SHOOTER')
    pygame.mouse.set_visible(False)

def resource():
    global font_size48, font_size20
    global sound_cheet, sound_damaged, sound_gameover, sound_weapon_1, sound_weapon_2
    global Image_bg_1, Image_bg_2, Image_heart
    global Image_player, Image_weapon_1, Image_weapon_2
    global Image_baddie, Image_meteor
    global playerRect

    pygame.mixer.music.load(WORKSPACE_SOUND + 'bgm.mp3')

    font_size48 = pygame.font.SysFont("comicsansms", 48)
    font_size20 = pygame.font.SysFont('hy견고딕', 20)

    sound_cheet = pygame.mixer.Sound(WORKSPACE_SOUND + 'sound_cheet.wav')
    sound_damaged = pygame.mixer.Sound(WORKSPACE_SOUND + 'sound_damaged.wav')
    sound_gameover = pygame.mixer.Sound(WORKSPACE_SOUND + 'sound_gameover.wav')
    sound_weapon_1 = pygame.mixer.Sound(WORKSPACE_SOUND + 'sound_weapon_1.wav')
    sound_weapon_2 = pygame.mixer.Sound(WORKSPACE_SOUND + 'sound_weapon_2.wav')

    Image_bg_1 = pygame.image.load(WORKSPACE_IMAGE + 'Image_bg_1.png')
    Image_bg_2 = pygame.image.load(WORKSPACE_IMAGE + 'Image_bg_2.png')
    Image_heart = pygame.image.load(WORKSPACE_IMAGE + 'Image_heart.png')

    Image_player = pygame.image.load(WORKSPACE_IMAGE + 'Image_player.png')
    Image_weapon_1 = pygame.image.load(WORKSPACE_IMAGE + 'Image_weapon_1.png')
    Image_weapon_2 = pygame.image.load(WORKSPACE_IMAGE + 'Image_weapon_2.png')
    Image_baddie = pygame.image.load(WORKSPACE_IMAGE + 'Image_baddie.png')
    Image_meteor = pygame.image.load(WORKSPACE_IMAGE + 'Image_meteor.png')

    playerRect = Image_player.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT : terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE : terminate()
                return

def draw_text(text, font, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    windowSurface.blit(textobj, textrect)

def draw_gamestart():
    global bgmState, topScore
    bgmState = 1
    topScore = 0
    pygame.mixer.music.play(-1, 0.0)
    windowSurface.blit(Image_bg_1, (0,0))
    draw_text('SHOOTER', font_size48, 180, 650)
    draw_text('Press a key to start.', font_size48, 80, 700)
    pygame.display.update()
    waitForPlayerToPressKey()

def draw_gameover():
    pygame.mixer.music.stop()
    sound_gameover.play()

    draw_text('GAME OVER', font_size48, 160, 300)
    draw_text('Press a key to play again.', font_size48, 30, 350)
    pygame.display.update()

    waitForPlayerToPressKey()

    sound_gameover.stop()
    bgmState = 2

def score_and_life(life, weaponType):
    draw_text(f'Score: {score}', font_size48, 10, 5)
    for i in range(life):
        windowSurface.blit(Image_heart, ((520-70*i),10))
    if weaponType % 2 == MISSILE:
        weaponText = 'MISSILE'
    else:
        weaponText = 'BOMB'
    draw_text(weaponText, font_size48, 10, 45)
    draw_text('Z : 공격', font_size20, 10, 110)
    draw_text('X : 치트', font_size20, 10, 135)
    draw_text('C : 체력 회복', font_size20, 10, 160)
    draw_text('V : 무기 전환', font_size20, 10, 185)

def make_baddie(baddies, baddieAddCounter):
    if baddieAddCounter % BADDIEADDCOUNT == 0:
        baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
        newBaddie = \
            {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
             'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
             'surface': pygame.transform.scale(Image_baddie,(baddieSize, baddieSize)),}
        baddies.append(newBaddie)
        return baddies

def move_baddie(baddies):
    for b in baddies:
        b['rect'].move_ip(0, b['speed'])

def remove_baddie(baddies):
    for b in baddies[:]: #copy
        if b['rect'].top > WINDOWHEIGHT:
            baddies.remove(b)
        return baddies

def make_meteor(meteors, meteorAddCounter):
    if meteorAddCounter % METEORADDCOUNT == 0:
        newMeteor = \
            {'rect': pygame.Rect(WINDOWWIDTH, random.randint(-METEORSIZE,350), METEORSIZE, METEORSIZE),
             'speed': random.randint(METEORMINSPEED, METEORMAXSPEED),
             'surface': pygame.transform.scale(Image_meteor,(METEORSIZE, METEORSIZE)),}
        meteors.append(newMeteor)
        return meteors

def move_meteor(meteors):
    for m in meteors:
        m['rect'].move_ip(-m['speed'], m['speed'])

def remove_meteor(meteors):
    for m in meteors[:]: #copy
        if m['rect'].top > WINDOWHEIGHT:
            meteors.remove(m)
        return meteors

def bullet_hit_baddie(bullets, baddies):
    for s in bullets:
        for b in baddies:
            if s['rect'].colliderect(b['rect']):
                bullets.remove(s)
                baddies.remove(b)
    return bullets, baddies

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            sound_damaged.play()
            baddies.remove(b)
            return True
    return False

def playerHasHitMeteor(playerRect, meteors):
    for m in meteors:
        if playerRect.colliderect(m['rect']):
            sound_damaged.play()
            meteors.remove(m)
            return True
    return False

def playerHasHitLaser(playerRect, lasers):
    for l in lasers:
        if playerRect.colliderect(l['rect']):
            sound_damaged.play()
            lasers.remove(l)
            return True
    return False

def show_background(starCount):
    windowSurface.blit(Image_bg_1, (0,starCount))
    if starCount < 800 :
        windowSurface.blit(Image_bg_2, (0,starCount-800))
    else:
        windowSurface.blit(Image_bg_2, (0,starCount % 800))
        windowSurface.blit(Image_bg_2, (0,starCount % 800 - 800))

def playBGM():
    if bgmState % 4 == 0 : pygame.mixer.music.play(-1, 0.0) # 짝수일 경우 재생

def trigger_boom():
    sound_cheet.play()
    for b in baddies[:]: #copy
        baddies.remove(b)
    for m in meteors[:]: #copy
        meteors.remove(m)

    return baddies, meteors

def make_bullet(playerRect, bullets, weaponType):
    if weaponType % 2 == MISSILE:
        sound_weapon_1.play()
        newBullet = \
            {'rect': pygame.Rect(playerRect.left + 14, playerRect.top - 32, 4, 32),
            'speed': 18,
            'surface': pygame.transform.scale(Image_weapon_1,(4, 32)),}
    elif weaponType % 2 == BOMB:
        sound_weapon_2.play()
        newBullet = \
            {'rect': pygame.Rect(playerRect.left, playerRect.top - 32, 32, 32),
            'speed': 8,
            'surface': pygame.transform.scale(Image_weapon_2,(32, 32)),}
    bullets.append(newBullet)
    return bullets

def move_bullet(bullets):
    for s in bullets:
        s['rect'].move_ip(0, -s['speed'])

def remove_bullet(bullets):
    for s in bullets[:]: #copy
        if s['rect'].top < 0:
            bullets.remove(s)
        return bullets

init()
resource()
draw_gamestart()
while True:
    if bgmState < 4:
        bgmState = 2 * bgmState
    else:
        bgmState = 4
    pygame.display.set_caption('최고 점수 : %s' % (topScore))

    bullets = []
    baddies = []
    meteors = []
    lasers = []

    score = 0
    life = 3
    weaponType = 0

    baddieAddCounter = 0
    meteorAddCounter = 0
    starCount = 0

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    playBGM()

    while True:
        score += 1
        baddieAddCounter += 1
        meteorAddCounter += 1
        starCount +=1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_z:
                    make_bullet(playerRect, bullets, weaponType)
                if event.key == K_x:
                    trigger_boom()
                if event.key == K_c:
                    if life < 3: life += 1
                if event.key == K_v:
                    weaponType += 1
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

        # playerRect.move_ip(x,y)
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERSPEED, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERSPEED, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERSPEED)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERSPEED)

        make_baddie(baddies, baddieAddCounter)
        move_baddie(baddies)
        remove_baddie(baddies)

        make_meteor(meteors, meteorAddCounter)
        move_meteor(meteors)
        remove_meteor(meteors)

        move_bullet(bullets)
        remove_bullet(bullets)
        bullet_hit_baddie(bullets, baddies)


        show_background(starCount) #background
        windowSurface.blit(Image_player, playerRect) #player
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect']) #baddie
        for m in meteors:
            windowSurface.blit(m['surface'], m['rect']) #meteor
        for s in bullets:
            windowSurface.blit(s['surface'], s['rect']) #bullet

        # windowSurface.blit(moon, (250,50)) #달
        score_and_life(life, weaponType)
        pygame.display.update()

        if playerHasHitBaddie(playerRect, baddies) \
        or playerHasHitMeteor(playerRect, meteors) \
        or playerHasHitLaser(playerRect, lasers):
            life -= 1
        if life == 0:
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)
    draw_gameover()