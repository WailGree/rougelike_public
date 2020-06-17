import copy
import random


def get_mob_position(borad, mob):
    mob_position = []
    try:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == mob:
                    mob_position.append((row, col))
    except IndexError:
        pass
    return mob_position


def get_row_position(position):
    return position[0]


def get_col_position(position):
    return position[1]


def is_valid_mob_position(board_width, board_height, position):
    mob_row_position = get_row_position(position)
    mob_col_position = get_col_position(position)
    if mob_row_position > 0 and mob_row_position < board_height - 1 and \
        mob_col_position > 0 and mob_col_position < board_width - 1:
        return True
    return False


def mob_random_step(position):
    directions = {
        'north': {
            'row_increment': -1,
            'col_increment': 0
        },
        'south': {
            'row_increment': 1,
            'col_increment': 0
        },
        'east': {
            'row_increment': 0,
            'col_increment': 1
        },
        'west': {
            'row_increment': 0,
            'col_increment': -1
        }
    }
    selected_direction = random.choice(list(directions.keys()))
    return get_row_position(position) + directions[selected_direction]['row_increment'],\
            get_col_position(position) + directions[selected_direction]['col_increment']

def mob_move(board, mob):
    board = copy.deepcopy(board)
    move = False
    try:
        board_width = len(board[0])
        board_height = len(board)
    except IndexError:
        return move, board
    if board_width < 3 or board_height < 3:
        return move, board
    mob_position = get_mob_position(board, mob)
    if len(mob_position) != 1:
        return move, board
    while True:
        mob_new_position = mob_random_step(mob_position[0])
        if is_valid_mob_position(board_width, board_height, mob_new_position):
            board[get_row_position(mob_position[0])][get_col_position(mob_position[0])],\
            board[get_row_position(mob_new_position)][get_col_position(mob_new_position)] = 0, mob
            break
    return True, board

board = [[0 for _ in range(5)] for _ in range(5)]
board[3][3] = 'x'
print(board)

mob_move(board, 'x')


"""
####
####
####
"""