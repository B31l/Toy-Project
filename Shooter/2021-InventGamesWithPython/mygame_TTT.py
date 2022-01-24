# 파이썬 게임 프로그래밍
# 2018225038 함수종

import pygame
import random
import time
import copy

def whoseLetter():
    if random.randint(0, 1) == 0:
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoseTurn():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, row_index, col_index, letter):
    board[row_index][col_index] = letter

def is_space_free(board, row_index, col_index):
    return board[row_index][col_index] == ' '

def is_winner(bo, le):
    return (bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or \
    (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or \
    (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or \
    (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or \
    (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or \
    (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or \
    (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or \
    (bo[2][0] == le and bo[1][1] == le and bo[0][2] == le)

def is_board_full(bo):
    return bo[0][0] != ' 'and \
    bo[0][1] != ' ' and \
    bo[0][2] != ' ' and \
    bo[1][0] != ' ' and \
    bo[1][1] != ' ' and \
    bo[1][2] != ' ' and \
    bo[2][0] != ' ' and \
    bo[2][1] != ' ' and \
    bo[2][2] != ' '

def computerAI(board, computerLetter):
    #승리
    for row_index in range(3):
        for col_index in range(3):
            boardcopy = copy.deepcopy(board)
            if is_space_free(boardcopy, row_index, col_index):
                makeMove(boardcopy, row_index, col_index, computerLetter)
                if is_winner(boardcopy, computerLetter):
                    return [row_index, col_index]
    
    #승리 방해
    for row_index in range(3):
        for col_index in range(3):
            boardcopy = copy.deepcopy(board)
            if is_space_free(boardcopy, row_index, col_index):
                makeMove(boardcopy, row_index, col_index, playerLetter)
                if is_winner(boardcopy, playerLetter):
                    return [row_index, col_index]

    boardcopy = copy.deepcopy(board)
    can_corners = []
    if is_space_free(boardcopy, 2, 0):
        can_corners.append(1)
    if is_space_free(boardcopy, 2, 2):
        can_corners.append(3)
    if is_space_free(boardcopy, 0, 0):
        can_corners.append(7)
    if is_space_free(boardcopy, 0, 2):
        can_corners.append(9)
    if len(can_corners) != 0:
        corner = random.choice(can_corners)
        if corner == 1:
            return [2, 0]
        elif corner == 3:
            return [2, 2]
        elif corner == 7:
            return [0, 0]    
        elif corner == 9:
            return [0, 2]
    elif is_space_free(boardcopy, 1, 1):
        return [1, 1]
    else:
        boardcopy = copy.deepcopy(board)
        can_sides = []
        if is_space_free(boardcopy, 2, 1):
            can_sides.append(2)
        if is_space_free(boardcopy, 1, 0):
            can_sides.append(4)
        if is_space_free(boardcopy, 1, 2):
            can_sides.append(6)
        if is_space_free(boardcopy, 0, 1):
            can_sides.append(8)
        if len(can_sides) != 0:
            side = random.choice(can_sides)
            if side == 2:
                return [2, 1]
            elif side == 4:
                return [1, 0]
            elif side == 6:
                return [1, 2]    
            elif side == 8:
                return [0, 1]

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

BG_COLOR = (0, 0, 0)                  # BLACK
GRID_COLOR = (66, 66, 66)             # GREY
PLAYER_COLOR = (0, 255, 255)          # BLUE
COMPUTER_COLOR = (255, 255, 255)      # WHITE
MSG_COLOR = (255, 0, 0)               # RED

large_font = pygame.font.SysFont('notosanscjkkr', 144)
end_font = pygame.font.SysFont('notosanscjkkr', 256)
CELL_SIZE = 200
PLAYER_WIN = 1
COMPUTER_WIN = 2
DRAW = 3
running = 0

board = [[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]

turn = whoseTurn()
playerLetter, computerLetter = whoseLetter()
while True: #게임 루프
    screen.fill(BG_COLOR)
    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and running == 0:
        col_index = event.pos[0] // CELL_SIZE
        row_index = event.pos[1] // CELL_SIZE
        print(col_index, row_index)

        if turn == 'player':    
            if is_space_free(board, row_index, col_index):
                makeMove(board, row_index, col_index, playerLetter) 

                if is_winner(board, playerLetter):
                    running = PLAYER_WIN
                elif is_board_full(board):
                    running = DRAW
                else:
                    turn = 'computer'

    if turn == 'computer' and running == 0: 
        row_index, col_index = computerAI(board, computerLetter)
        makeMove(board, row_index, col_index, computerLetter)

        if is_winner(board, computerLetter):
            running = COMPUTER_WIN 
        elif is_board_full(board):
            running = DRAW
        else:
            turn = 'player'


    #화면 그리기
    #격자 그리기
    for row_index in range(3): # col_count
        for col_index in range(3): # row_count
            pygame.draw.rect(screen, GRID_COLOR, pygame.Rect(col_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE), 5)

    #Letter 그리기
    for row_index in range(3):
        for col_index in range(3):
            letter = board[row_index][col_index]
            if letter == playerLetter:
                PLAYER_image = large_font.render(playerLetter, True, PLAYER_COLOR)
                screen.blit(PLAYER_image, PLAYER_image.get_rect(centerx=col_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) 
            elif letter == computerLetter:
                COMPUTER_image = large_font.render(computerLetter, True, COMPUTER_COLOR)
                screen.blit(COMPUTER_image, COMPUTER_image.get_rect(centerx=col_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) 
    
    #게임종료 메세지 그리기
    if running > 0: 
        if running == PLAYER_WIN:
            player_win_image = end_font.render('WIN', True, MSG_COLOR) # True는 글자를 부드럽게 해 주는 안티알라이싱
            screen.blit(player_win_image, player_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        elif running == COMPUTER_WIN:
            computer_win_image = end_font.render('LOSE', True, MSG_COLOR)
            screen.blit(computer_win_image, computer_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        else:
            draw_image = end_font.render('DRAW', True, MSG_COLOR)
            screen.blit(draw_image, draw_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(30) #30 FPS

pygame.quit() 