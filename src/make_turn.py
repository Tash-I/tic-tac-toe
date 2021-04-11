from constants import BOARD_SIZE

def make_turn(x_or_o):

    print(f'{x_or_o}\'s turn')
    row = input(f'enter a row number: ')

    if not row.isdigit() or int(row) not in range(1, BOARD_SIZE + 1):
        print(f'Input "{row}" is not a digit from 1 to 3')
        return make_turn(x_or_o)

    column = input(f'enter a column number: ')
    if not column.isdigit() or int(column) not in range(1, BOARD_SIZE + 1):
        print(f'Input "{column}" is not a digit from 1 to {BOARD_SIZE}')
        return make_turn(x_or_o)

    return int(row), int(column)
