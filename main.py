import minimax
import game_utils
import numpy as np

board = [
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [-1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1],
]

board = np.array(board)
game_utils.checkers.print_board(board)
