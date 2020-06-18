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
import WailGree
from random import randint

# [room[exit pos x,exit pos y,enter pos x,enter pos y]]
door_positions = [[6, 29, 0, 0], [1, 0, 22, 5], [
    0, 5, 7, 0], [13, 17, 13, 0]]


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


def check_player_has_key(backpack, map_number, row, col, door_positions):
    new_map_number = next_map_numer(map_number, row, col, door_positions)
    if '🗝️ ' in backpack.keys():
        if backpack['🗝️ '] >= new_map_number-1:
            return True
    return False


def next_map_numer(map_number, row, col, door_positions):
    if map_number == 1:
        new_map_number = map_number + 1
    elif row == door_positions[map_number-1][0] and col == door_positions[map_number-1][1]:
        new_map_number = map_number - 1
    elif row == door_positions[map_number-1][2] and col == door_positions[map_number-1][3]:
        new_map_number = map_number + 1
    return new_map_number


def print_win_or_lose(action):
    if action == 'win':
        print('''
▓██   ██▓ ▒█████   █    ██      █     █░  ██▓ ███▄    █ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒    ▓█░ █ ░█░▒▓██▒ ██ ▀█   █ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░    ▒█░ █ ░█ ▒▒██▒▓██  ▀█ ██▒
  ░ ▐██▓░▒██   ██░▓▓█  ░██░    ░█░ █ ░█ ░░██░▓██▒  ▐▌██▒
  ░ ██▒▓░░ ████▓▒░▒▒█████▓     ░░██▒██▓ ░░██░▒██░   ▓██░
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ░ ▓░▒ ▒   ░▓  ░ ▒░   ▒ ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░       ▒ ░ ░  ░ ▒ ░░ ░░   ░ ▒░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░       ░   ░  ░ ▒ ░   ░   ░ ░ 
 ░ ░         ░ ░     ░             ░      ░           ░ 

        ''')
    elif action == 'lose':
        print('''
▓██   ██▓ ▒█████   █    ██       ██▓    ▒█████    ██████  ▓█████
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒     ▓██▒   ▒██▒  ██▒▒██    ▒  ▓█   ▀
  ▒██ ██░▒██░  ██▒▓██  ▒██░     ▒██░   ▒██░  ██▒░ ▓██▄    ▒███  
  ░ ▐██▓░▒██   ██░▓▓█  ░██░     ▒██░   ▒██   ██░  ▒   ██▒ ▒▓█  ▄
  ░ ██▒▓░░ ████▓▒░▒▒█████▓     ▒░██████░ ████▓▒░▒██████▒▒▒░▒████
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ░░ ▒░▓  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░░ ▒░ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░░ ░ ▒    ░ ▒ ▒░ ░ ░▒  ░ ░░ ░ ░  
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░        ░ ░  ░ ░ ░ ▒  ░  ░  ░      ░  
 ░ ░         ░ ░     ░         ░    ░      ░ ░        ░  ░   ░  

        ''')


def collect_stuffs(board, row, col, player):    # of the next step col/row
    backpack = main.backpack
    if board[row][col] == '🗝️ ':
        if '🗝️ ' in backpack.keys():
            backpack['🗝️ '] += 1
        else:
            backpack.update({'🗝️ ': 1})
    elif board[row][col] == '🤕':
        if '🤕' in backpack.keys():
            backpack['🤕'] += 1
        else:
            backpack.update({'🤕': 1})
        player['HP'] -= randint(1, 3)
    elif board[row][col] == '🗡️ ':
        if '🗡️ ' in backpack.keys():
            backpack['🗡️ '] += 1
        else:
            backpack.update({'🗡️ ': 1})
        player['damage'] += randint(1, 7)
    elif board[row][col] == '🛡️ ':
        if '🛡️ ' in backpack.keys():
            backpack['🛡️ '] += 1
        else:
            backpack.update({'🛡️ ': 1})
        player['armor'] += randint(1, 7)
    elif board[row][col] == '🐲':
        if '🐲' in backpack.keys():
            backpack['🐲'] += 1
        else:
            backpack.update({'🐲': 1})
        player['armor'] -= randint(1, 4)
    elif board[row][col] == '💊':
        if '💊' in backpack.keys():
            backpack['💊'] += 1
        else:
            backpack.update({'💊': 1})
        player['HP'] += randint(1, 7)
    return backpack, player


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
        engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), new_map_number, main.generate_mob(new_map_number))
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
    elif map_number == 5:
        print_win_or_lose('win')
        quit()
    return BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y


def battle(board, next_row, next_col, player, mob):
    player_icon = player['icon']
    mob_icon = mob['icon']
    if ((player_icon == '🧝' or player_icon == '👨' or player_icon == '🙇') and board[next_row][next_col] == mob_icon) or ((mob_icon == '💀' or mob_icon == '👿' or mob_icon == '👺' or mob_icon == '👽') and board[next_row][next_col] == player_icon):
        player = WailGree.in_combat(player, mob)
        if player['HP'] == 0:
            print_win_or_lose('lose')
            quit()  # GAME OVER update player details
        return True, player
    return False, player


def potter_wall(player, map_number, board, row, col, next_row, next_col):
    if chech_is_door(map_number, door_positions, board, next_row, next_col):
        return False
    elif next_row == 19 and next_col == 27 and map_number == 1:
        return True
    elif next_row == 0 and next_col == 15 and map_number == 4:
        return True


def move_depending_on_key(player, map_number, board, row, col, next_row, next_col, mob):
    backpack, player = collect_stuffs(board, next_row, next_col, player)
    something, player = battle(board, next_row, next_col, player, mob)
    if checking_is_wall(board, next_row, next_col) is False:
        board[next_row][next_col] = board[row][col]
        if chech_is_door(map_number, door_positions, board, row, col):
            board[row][col] = '🚪'
        else:
            board[row][col] = 0
        board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
        return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
    else:
        if potter_wall(player['icon'], map_number, board, row, col, next_row, next_col):
            if map_number == 1:
                map_number = 4
                BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y = map_details(
                    map_number)
                board2 = generate_stuffs(
                    engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), map_number, main.generate_mob(map_number))
                PLAYER_START_X2, PLAYER_START_Y2 = 0, 15
            elif map_number == 4:
                map_number = 1
                BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y = map_details(
                    map_number)
                board2 = generate_stuffs(
                    engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), map_number, main.generate_mob(map_number))
                PLAYER_START_X2, PLAYER_START_Y2 = 19, 27
            # generate 4.th room
            return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack
        elif chech_is_door(map_number, door_positions, board, next_row, next_col) and check_player_has_key(backpack, map_number, next_row, next_col, door_positions):
            board[next_row][next_col] = board[row][col]
            board[row][col] = 0
            board, PLAYER_START_X, PLAYER_START_Y, map_number = next_map(
                map_number, player, door_positions, next_row, next_col)
            return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack
        else:
            board2, PLAYER_START_X2, PLAYER_START_Y2 = 0, 0, 0
            return board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack


def move_player(key, board, player, map_number, mob):
    width = len(board[0])
    height = len(board)
    for h in range(height):
        for w in range(width):
            if board[h][w] == player['icon']:
                row = h
                col = w
    if key == 'w':
        if row - 1 >= 0:
            board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack = move_depending_on_key(
                player, map_number, board, row, col, row-1, col, mob)
    elif key == 's':
        if row + 1 < height:
            board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack = move_depending_on_key(
                player, map_number, board, row, col, row+1, col, mob)
    elif key == 'a':
        if col - 1 >= 0:
            board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack = move_depending_on_key(
                player, map_number, board, row, col, row, col-1, mob)
    elif key == 'd':
        if col + 1 < width:
            board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack = move_depending_on_key(
                player, map_number, board, row, col, row, col+1, mob)
    return board, PLAYER_START_X, PLAYER_START_Y, map_number, backpack


def generate_stuffs(board, map_number, mob):
    width = len(board[0])
    height = len(board)
    characters = ['🐲', '🛡️ ', '🗡️ ', '💊', '🤕']
    for element in characters:
        board[randint(1, height-2)][randint(1, width-2)] = element
    if map_number == 1:
        board[door_positions[0][0]][door_positions[0][1]] = '🚪'
        if '🗝️ ' not in main.backpack.keys():
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
        board[randint(1, height-2)][randint(1, width-2)] = mob['icon']
    elif map_number == 2:
        board[door_positions[1][0]][door_positions[1][1]] = '🚪'
        board[door_positions[1][2]][door_positions[1][3]] = '🚪'
        board[randint(1, height-2)][randint(1, width-2)] = mob['icon']
        if '🗝️ ' in main.backpack.keys():
            if main.backpack['🗝️ '] == 1:
                board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
        else:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
    elif map_number == 3:
        board[door_positions[2][0]][door_positions[2][1]] = '🚪'
        board[door_positions[2][2]][door_positions[2][3]] = '🚪'
        board[randint(1, height-2)][randint(1, width-2)] = mob['icon']
        if '🗝️ ' in main.backpack.keys():
            if main.backpack['🗝️ '] == 2:
                board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
        else:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
    elif map_number == 4:
        board[door_positions[3][0]][door_positions[3][1]] = '🚪'
        board[door_positions[3][2]][door_positions[3][3]] = '🚪'
        board[randint(1, height-2)][randint(1, width-2)] = mob['icon']
        if '🗝️ ' in main.backpack.keys():
            if main.backpack['🗝️ '] == 3:
                board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
        else:
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
            board[randint(1, height-2)][randint(1, width-2)] = '🗝️ '
    return board
