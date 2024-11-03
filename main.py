import minimax
import game_utils
import numpy as np

# initial_board = [
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [-1, 0, -1, 0, -1, 0],
#     [0, -1, 0, -1, 0, -1],
# ]

# initial_board = [
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1],
#     [0, 0, -1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [-1, 0, -1, 0, -1, 0],
#     [0, 0, 0, -1, 0, 0],
# ]

# initial_board = [
#     [0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, -1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, -1, 0, -1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, -1, 0, -1, 0, -1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, -1, 0, 0, 0, 0, 0],
# ]

# initial_board = [
#     [0, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [-1, 0, -1, 0, -1, 0, -1, 0],
#     [0, -1, 0, -1, 0, -1, 0, -1],
#     [-1, 0, -1, 0, -1, 0, -1, 0],
# ]

# initial_board = [
#     [0, -1, 0, -1, 0, -1, 0, -1],
#     [-1, 0, -1, 0, -1, 0, -1, 0],
#     [0, -1, 0, -1, 0, -1, 0, -1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0],
# ]

# initial_board = [
#     [0, 0, 0, 0, 0, -1, 0, -1],
#     [-1, 0, -1, 0, -1, 0, -1, 0],
#     [0, 0, 0, -1, 0, -1, 0, -1],
#     [-1, 0, -1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 0],
#     [1, 0, 1, 0, 0, 0, 0, 0],
# ]

initial_board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -2, 0],
    [0, 0, 0, 0],
]

initial_board = np.array(initial_board)

print("initial board")
game_utils.checkers.print_board(initial_board)
initial_board = np.rot90(initial_board, 2)
print()

# boards = minimax.get_all_legal_boards(initial_board, -1)
# for board in boards:
#     board = np.rot90(board, 2)
#     game_utils.checkers.print_board(board)
#     print()


board = minimax.get_best_move(initial_board, -1, depth=0)
board = np.rot90(board, 2)
game_utils.checkers.print_board(board)
