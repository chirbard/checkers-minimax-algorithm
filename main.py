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

initial_board = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]

# initial_board = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, -1, 0],
#     [0, 0, 0, 0],
# ]

initial_board = np.array(initial_board)

print("initial board")
game_utils.checkers.print_board(initial_board)
initial_board = np.rot90(initial_board, 2)
print()

# boards = minimax.get_all_legal_boards(initial_board, -1)
# for board in boards:
#     game_utils.checkers.print_board(np.rot90(board, 2))
#     print()

#     boards2 = minimax.get_all_legal_boards(board, -1)
#     for board2 in boards2:
#         game_utils.checkers.print_board(np.rot90(board2, 2))
#         print()

# game_utils.checkers.print_board(board)
# print()


board = minimax.get_best_move(initial_board, -1, depth=2)
board = np.rot90(board, 2)
game_utils.checkers.print_board(board)
