def display_board(board):
    print('\n')

    for i in range(len(board)):
        row_values = [f' {board[i][j]} ' for j in range(len(board))]
        print('|'.join(row_values))
        if i < len(board) - 1:
            print('--- ' * len(board))

    print('\n')
