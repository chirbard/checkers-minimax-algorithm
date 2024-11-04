from minimax import Minimax
import game_utils
import numpy as np


initial_board = np.array([
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
])


print("initial board:")
game_utils.checkers.print_board(initial_board)

print("best move:")
new_board = Minimax.get_best_move(initial_board, 1, depth=2)
game_utils.checkers.print_board(new_board)
