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


import engine
import main
from random import randint

# [room[exit pos x,exit pos y,enter pos x,enter pos y]]
door_positions = [[6, 29, 0, 0], [1, 0, 22, 5], [
    0, 5, 7, 0], [13, 17, 0, 0]]


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
    elif row == door_positions[map_number-1][2] and col == door_positions[map_number-1][3]:
        return True
    else:
        return False


def check_player_has_key(backpack, map_number):
    if '🗝️ ' in backpack.keys():
        if backpack['🗝️ '] >= map_number:
            return True
    return False


def collect_stuffs(board, row, col):    # of the next step col/row
    backpack = main.backpack
    if board[row][col] == '🗝️ ':
        if '🗝️ ' in backpack.keys():
            backpack['🗝️ '] += 1
        else:
            backpack.update({'🗝️ ': 1})
    elif board[row][col] == '💀':
        if '💀' in backpack.keys():
            backpack['💀'] += 1
        else:
            backpack.update({'💀': 1})
    elif board[row][col] == '🤕':
        if '🤕' in backpack.keys():
            backpack['🤕'] += 1
        else:
            backpack.update({'🤕': 1})
    elif board[row][col] == '🗡️ ':
        if '🗡️ ' in backpack.keys():
            backpack['🗡️ '] += 1
        else:
            backpack.update({'🗡️ ': 1})
    elif board[row][col] == '🛡️ ':
        if '🛡️ ' in backpack.keys():
            backpack['🛡️ '] += 1
        else:
            backpack.update({'🛡️ ': 1})
    elif board[row][col] == '🐲':
        if '🐲' in backpack.keys():
            backpack['🐲'] += 1
        else:
            backpack.update({'🐲': 1})
    elif board[row][col] == '💊':
        if '💊' in backpack.keys():
            backpack['💊'] += 1
        else:
            backpack.update({'💊': 1})
    return backpack


def next_map(map_number, player, door_positions, row, col):
    if map_number == 1:
        new_map_number = map_number + 1
    elif row == door_positions[map_number-1][0] and col == door_positions[map_number-1][1]:
        new_map_number = map_number - 1
    elif row == door_positions[map_number-1][2] and col == door_positions[map_number-1][3]:
        new_map_number = map_number + 1
    BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y = map_details(
        new_map_number)
    board = generate_stuffs(
        engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), new_map_number)
    if new_map_number < map_number:
        PLAYER_START_X, PLAYER_START_Y = room_back(new_map_number, map_number)
    return board, PLAYER_START_X, PLAYER_START_Y, new_map_number
    # main_test.game(map_number, player)


def room_back(new_map_number, map_number):
    if map_number == 2 and new_map_number == 1:
        PLAYER_START_X, PLAYER_START_Y = 6, 28
    elif map_number == 3 and new_map_number == 2:
        PLAYER_START_X, PLAYER_START_Y = 21, 5
    elif map_number == 4 and new_map_number == 3:
        PLAYER_START_X, PLAYER_START_Y = 7, 1
    return PLAYER_START_X, PLAYER_START_Y


def map_details(map_number):
    if map_number == 1:
        BOARD_WIDTH, BOARD_HEIGHT = 30, 20
        PLAYER_START_X, PLAYER_START_Y = 3, 3
    elif map_number == 2:
        BOARD_WIDTH, BOARD_HEIGHT = 14, 23
        PLAYER_START_X, PLAYER_START_Y = 1, 1
    elif map_number == 3:
        BOARD_WIDTH, BOARD_HEIGHT = 9, 9
        PLAYER_START_X, PLAYER_START_Y = 1, 5
    elif map_number == 4:
        BOARD_WIDTH, BOARD_HEIGHT = 18, 15
        PLAYER_START_X, PLAYER_START_Y = 13, 16
    return BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y


def move_player(key, board, player, map_number):
    width = len(board[0])
    height = len(board)
    for h in range(height):
        for w in range(width):
            if board[h][w] == player:
                row = h
                col = w
    if key == 'w':
        if row - 1 >= 0:
            backpack = collect_stuffs(board, row-1, col)
            if checking_is_wall(board, row-1, col) is False:
                board[row-1][col] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
                board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
            else:
                if chech_is_door(map_number, door_positions, board, row-1, col) and check_player_has_key(backpack, map_number):
                    board[row-1][col] = board[row][col]
                    board[row][col] = 0
                    board, PLAYER_START_X, PLAYER_START_Y, map_number = next_map(
                        map_number, player, door_positions, row-1, col)
                    return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack
                else:
                    board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                    return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
    elif key == 's':
        if row + 1 < height:
            backpack = collect_stuffs(board, row+1, col)
            if checking_is_wall(board, row+1, col) is False:
                board[row+1][col] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
                board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
            else:
                if chech_is_door(map_number, door_positions, board, row+1, col) and check_player_has_key(backpack, map_number):
                    board[row+1][col] = board[row][col]
                    board[row][col] = 0
                    board, PLAYER_START_X, PLAYER_START_Y, map_number = next_map(
                        map_number, player, door_positions, row+1, col)
                    return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack
                else:
                    board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                    return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
    elif key == 'a':
        if col - 1 >= 0:
            backpack = collect_stuffs(board, row, col-1)
            if checking_is_wall(board, row, col-1) is False:
                board[row][col-1] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
                board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
            else:
                if chech_is_door(map_number, door_positions, board, row, col-1) and check_player_has_key(backpack, map_number):
                    board[row][col-1] = board[row][col]
                    board[row][col] = 0
                    board, PLAYER_START_X, PLAYER_START_Y, map_number = next_map(
                        map_number, player, door_positions, row, col-1)
                    return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack
                else:
                    board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                    return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
    elif key == 'd':
        if col + 1 < width:
            backpack = collect_stuffs(board, row, col+1)
            if checking_is_wall(board, row, col+1) is False:
                board[row][col+1] = board[row][col]
                if chech_is_door(map_number, door_positions, board, row, col):
                    board[row][col] = '🚪'
                else:
                    board[row][col] = 0
                board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
            else:
                if chech_is_door(map_number, door_positions, board, row, col+1) and check_player_has_key(backpack, map_number):
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0
                    board, PLAYER_START_X, PLAYER_START_Y, map_number = next_map(
                        map_number, player, door_positions, row, col+1)
                    return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack
                else:
                    board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
                    return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack


def generate_stuffs(board, map_number):
    width = len(board[0])
    height = len(board)
    if map_number == 1:
        board[door_positions[0][0]][door_positions[0][1]] = '🚪'
        if main.visited_rooms == 0:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            main.visited_rooms += 1
    elif map_number == 2:
        board[door_positions[1][0]][door_positions[1][1]] = '🚪'
        board[door_positions[1][2]][door_positions[1][3]] = '🚪'
        if main.visited_rooms == 1:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            main.visited_rooms += 1
    elif map_number == 3:
        board[door_positions[2][0]][door_positions[2][1]] = '🚪'
        board[door_positions[2][2]][door_positions[2][3]] = '🚪'
        if main.visited_rooms == 2:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            main.visited_rooms += 1
    elif map_number == 4:
        board[door_positions[3][0]][door_positions[3][1]] = '🚪'
        if main.visited_rooms == 3:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            main.visited_rooms += 1

    
    board[randint(1, height-2)][randint(1, width-2)] = '💀'
    board[randint(1, height-2)][randint(1, width-2)] = '🤕'
    board[randint(1, height-2)][randint(1, width-2)] = '💊'
    board[randint(1, height-2)][randint(1, width-2)] = '🗡️ '
    board[randint(1, height-2)][randint(1, width-2)] = '🛡️ '
    board[randint(1, height-2)][randint(1, width-2)] = '🐲'
    return board
