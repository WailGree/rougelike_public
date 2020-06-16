def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    width = len(board[0])
    height = len(board)

    for h in range(height):
        for w in range(width):
            if board[h][w] != 0:
                print(board[h][w], end='')
            elif w == 0 or w == width-1:
                print('🧱', end='')
            elif h == height-1 or h == 0:
                print('🧱', end=' ')
            elif board[h][w] == 0:
                print(' ', end=' ')
            else:
                print(board[h][w], end=' ')
        print()
