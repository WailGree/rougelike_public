# Máté's working file
# 🧱🚪🔄❎
'''
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🧱                                                          🧱
🧱                                                          🧱
🧱                                                          🧱
🧱                                                          🧱
🧱                                                          🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱
🧱                                                          🚪🚪                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱                                                          🧱🧱                         🧱
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱                         🧱
🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱                         🧱
                         🧱                                 🧱🧱                         🧱
                         🧱                                 🧱🧱                         🧱
                         🧱                                 🧱🧱                         🧱
                         🧱                                 🧱🧱                         🧱
                         🧱                                 🧱🧱🧱🧱🧱🧱🚪🧱🧱🧱🧱🧱🧱🧱🧱
                         🧱                                 🧱🧱🧱🧱🧱🧱🚪🧱🧱🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🧱🧱               🧱
                         🧱                                 🚪🚪               🧱
                         🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱


    A
   DBC


'''

# ui.display_board(board)
import ui
import engine
from random import randint


# board = engine.create_board(30, 20)

# board[15][29] = '🚪'
# board[15][2] = '🗝️ '
# board[14][4] = '💀'
# board[2][7] = '🤕'
# board[5][9] = '💊'
# board[14][15] = '🗡️ '
# board[10][9] = '🛡️ '
# board[13][2] = '🐲'


# def display_board(board):   # ui
#     width = len(board[0])
#     height = len(board)

#     for h in range(height):
#         for w in range(width):
#             if board[h][w] != 0:
#                 print(board[h][w], end='')
#             elif h == 0 or w == 0 or h == height-1 or w == width-1:
#                 print('🧱', end='')
#             elif board[h][w] == 0:
#                 print(' ', end=' ')
#             else:
#                 print(board[h][w], end=' ')
#         print()


# ui.display_board(board)


# [room number][enter door x, enter door y,exit door x, exit door y]
door_positions = [[6, 29, 0, 0], [1, 1, 22, 5], [
    0, 9, 7, 0], [17, 13, 0, 0]]    # !!!!!!!!!!!!!!!!
map_number = 1


def checking_is_wall(board, row, col):
    width = len(board[0])
    height = len(board)
    if row == height-1 or col == width-1:
        return True
    elif row == 0 or col == 0:
        return True
    else:
        return False


def chech_is_door(map_number, door_positions, board, row, col):
    if row == door_positions[map_number-1][0] and col == door_positions[map_number-1][1]:
        return True
    else:
        return False


def move_player(key, board, player):
    width = len(board[0])
    height = len(board)

    for h in range(height):
        for w in range(width):
            if board[h][w] == player:
                row = h
                col = w
    if key == 'w':
        if row - 1 >= 0:
            if checking_is_wall(board, row-1, col) is False:
                board[row-1][col] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
            else:
                if chech_is_door(map_number, door_positions, board, row-1, col):
                    board[row-1][col] = board[row][col]
                    board[row][col] = 0
                    game(1, player)
    elif key == 's':
        if row + 1 < height:
            if checking_is_wall(board, row+1, col) is False:
                board[row+1][col] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
            else:
                if chech_is_door(map_number, door_positions, board, row+1, col):
                    board[row+1][col] = board[row][col]
                    board[row][col] = 0
    elif key == 'a':
        if col - 1 >= 0:
            if checking_is_wall(board, row, col-1) is False:
                board[row][col-1] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
            else:
                if chech_is_door(map_number, door_positions, board, row, col-1):
                    board[row][col-1] = board[row][col]
                    board[row][col] = 0
    elif key == 'd':
        if col + 1 < width:
            if checking_is_wall(board, row, col+1) is False:
                board[row][col+1] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
            else:
                if chech_is_door(map_number, door_positions, board, row, col+1):
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0


def generate_stuffs(board, map_number=1):
    width = len(board[0])
    height = len(board)
    if map_number == 1:
        board[door_positions[0][0]][door_positions[0][1]] = '🚪'
    elif map_number == 2:
        board[door_positions[1][0]][door_positions[1][1]] = '🚪'
    elif map_number == 3:
        board[door_positions[2][0]][door_positions[2][1]] = '🚪'
    elif map_number == 4:
        board[door_positions[3][0]][door_positions[3][1]] = '🚪'

    board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
    board[randint(1, height-2)][randint(1, width-2)] = '💀'
    board[randint(1, height-2)][randint(1, width-2)] = '🤕'
    board[randint(1, height-2)][randint(1, width-2)] = '💊'
    board[randint(1, height-2)][randint(1, width-2)] = '🗡️ '
    board[randint(1, height-2)][randint(1, width-2)] = '🛡️ '
    board[randint(1, height-2)][randint(1, width-2)] = '🐲'
    return board

# ui.display_board(board)
