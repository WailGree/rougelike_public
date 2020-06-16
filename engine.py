def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    return [[0 for x in range(width)] for y in range(height)]


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
        width = len(board[0])
    height = len(board)
    is_in_board = False
    for h in range(height):
        for w in range(width):
            if board[h][w] == player:
                is_in_board = True
                break
    if is_in_board is False:        
        board[x][y] = player

