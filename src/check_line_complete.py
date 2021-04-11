from constants import BOARD_SIZE, X, O

def check_line_complete(line):
    if line.count(X) == BOARD_SIZE:
        return X
    if line.count(O) == BOARD_SIZE:
        return O
    return False
