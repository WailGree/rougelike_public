import copy
import random


def get_mob_position(board, mob):
    mob_position = []
    for row in range(get_board_rows(board)):
        for col in range(get_borad_cols(board)):
                if board[row][col] == mob:
                    mob_position.append((row, col))
    return mob_position


def get_board_rows(board):
    return len(board)


def get_borad_cols(board):
    try:
        return len(board[0])
    except IndexError:
        return 0


def get_row_position(position):
    return position[0]


def get_col_position(position):
    return position[1]


def is_valid_mob_position(board_cols, board_rows, position):
    mob_row_position = get_row_position(position)
    mob_col_position = get_col_position(position)
    if mob_row_position > 0 and mob_row_position < board_rows - 1 and \
        mob_col_position > 0 and mob_col_position < board_cols - 1:
        return True
    else:
        return False


def mob_random_step(position):
    DIRECTIONS = {
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
    selected_direction = random.choice(list(DIRECTIONS.keys()))
    return get_row_position(position) + DIRECTIONS[selected_direction]['row_increment'],\
            get_col_position(position) + DIRECTIONS[selected_direction]['col_increment']


def mob_move(board, mob):
    WALL_TOP_WIDTH = 1
    WALL_BOTTOM_WIDTH = 1
    WALL_LEFT_WIDTH = 1
    WALL_RIGHT_WIDTH = 1

    board = copy.deepcopy(board)
    board_cols = get_borad_cols(board)
    board_rows = get_board_rows(board)
    if board_cols <= (WALL_LEFT_WIDTH + WALL_RIGHT_WIDTH) or \
        board_rows <= (WALL_TOP_WIDTH + WALL_BOTTOM_WIDTH):
        return False, board
    mob_position = get_mob_position(board, mob)
    if len(mob_position) != 1:
        return False, board
    valid_new_step = False
    while valid_new_step is False:
        mob_new_position = mob_random_step(mob_position[0])
        if is_valid_mob_position(board_cols, board_rows, mob_new_position):
            board[get_row_position(mob_position[0])][get_col_position(mob_position[0])],\
            board[get_row_position(mob_new_position)][get_col_position(mob_new_position)] = 0, mob
            valid_new_step = True
    return True, board
    