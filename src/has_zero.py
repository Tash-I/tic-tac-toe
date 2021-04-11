from constants import EMPTY

def has_zero(board):
    for row in board:
        if EMPTY in row:
            return True
    return False
