# 파이썬 게임 프로그래밍 2021
# 인공지능 vs 인공지능
# X는 5단계로 구성된 인공지능입니다.
#   승리->승리방해->corners->center->sides
# O는 3단계로 구성된 인공지능입니다.
#   승리->승리방해->random

import random

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'turn_x'
    else:
        return 'turn_o'

def makeMove(board, letter, move):
  board[move] = letter

def isWinner(bo, le):
  return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def isBoardFull(board):
  # Return True if every space on the board has been taken. Otherwise, return False
  for i in range(1, 10):
    if isSpaceFree(board, i):
      return False
  return True

def getBoardCopy(board):
  boardCopy = []
  for i in board:
    boardCopy.append(i)
  return boardCopy

def isSpaceFree(board, move):
  return board[move] == ' '

def chooseRandomMoveFromList(board, movesList):
  possibleMoves = []
  for i in movesList:
    if isSpaceFree(board, i):
      possibleMoves.append(i)

  if len(possibleMoves) != 0: 
    return random.choice(possibleMoves)
  else:
    return None

def get_x_move(board):
  for i in range(1, 10):
    boardCopy = getBoardCopy(board)
    if isSpaceFree(boardCopy, i):
      makeMove(boardCopy, 'X', i)
      if isWinner(boardCopy, 'X'):
        return i
  for i in range(1, 10):
    boardCopy = getBoardCopy(board)
    if isSpaceFree(boardCopy, i):
      makeMove(boardCopy, 'O', i)
      if isWinner(boardCopy, 'O'):
        return i
  move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
  if move != None:
    return move
  if isSpaceFree(board, 5):
    return 5
  return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def get_o_move(board):
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, 'O', i)
            if isWinner(boardCopy, 'O'):
                return i
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, 'X', i)
            if isWinner(boardCopy, 'X'):
                return i
    return chooseRandomMoveFromList(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def printIsWinner(winner):
    if winner == 'X': # X 승
        print('X', end='')
    elif winner == 'O': # O 승
        print('O', end='')
    else:
        print('T', end='') # 무승부

def printNewline(count):
    if count % 100 == 0:
        print('')

def printOutput():
    print('X의 승리 횟수 : ' + str(count_x) + '\n')
    print('O의 승리 횟수 : ' + str(count_o) + '\n')
    print('무승부 횟수 : ' + str(count_t))
    

count = 0          # 줄바꿈
count_x = 0        # X 승리
count_o = 0        # O 승리
count_t = 0        # 무승부
winner = ' '
while count <= 10001:
    count += 1
    theBoard = [' '] * 10
    x_Letter, o_Letter = ['X','O']
    turn = whoGoesFirst()
    running = True

    while running:
        if turn == 'turn_x':
            move = get_x_move(theBoard)
            makeMove(theBoard, 'X', move)
            if isWinner(theBoard, 'X'):
                count_x += 1
                winner = 'X'
                running = False
            elif isBoardFull(theBoard):
                count_t += 1
                winner = 'T'
                running = False
            else:
                turn = 'turn_o'

        elif turn == 'turn_o':
            move = get_o_move(theBoard)
            makeMove(theBoard, 'O', move)
            if isWinner(theBoard, 'O'):
                count_o += 1
                winner = 'O'
                running = False
            elif isBoardFull(theBoard):
                count_t += 1
                winner = 'T'
                running = False
            else:
                turn = 'turn_x'
    printIsWinner(winner)
    printNewline(count)
printOutput()