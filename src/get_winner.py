from constants import BOARD_SIZE
from check_line_complete import check_line_complete

def get_winner(board):

    for i in range(BOARD_SIZE):

        row_check_result = check_line_complete(board[i])
        if row_check_result:
            return row_check_result

        column_check_result = check_line_complete([row[i] for row in board])
        if column_check_result:
            return column_check_result

    main_diagonal = [board[i][i] for i in range(BOARD_SIZE)]
    main_diagonal_check_result = check_line_complete(main_diagonal)
    if main_diagonal_check_result:
        return main_diagonal_check_result

    antidiagonal = [board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)]
    antidiagonal_check_result = check_line_complete(antidiagonal)
    if antidiagonal_check_result:
        return antidiagonal_check_result

    return None
