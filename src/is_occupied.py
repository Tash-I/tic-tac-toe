from constants import EMPTY

def is_occupied(board, row, column):
    if board[row - 1][column - 1] != EMPTY:
        print(f'The cell {row} - {column} is already occupied')
        return False
    return True
