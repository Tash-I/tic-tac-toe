from constants import BOARD_SIZE, EMPTY, X, O
from has_zero import has_zero
from make_turn import make_turn
from is_occupied import is_occupied
from get_winner import get_winner
from display_result import display_result
from is_game_on import is_game_on
from display_board import display_board

def start_game():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    actor = X

    winner = None
    while has_zero(board) and not winner:
        (row, column) = make_turn(actor)

        if is_occupied(board, row, column):
            board[row - 1][column - 1] = actor
            actor = X if actor == O else O
        else:
            (row, column) = make_turn(actor)


        display_board(board)

        winner = get_winner(board)


    display_result(winner)

    if is_game_on():
        start_game()
    else:
        print('Game over')
