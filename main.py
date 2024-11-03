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

initial_board = np.array(initial_board)

print("initial board")
game_utils.checkers.print_board(initial_board)
initial_board = np.rot90(initial_board, 2)
print()

# minimax.get_all_legal_moves(board, 1)
# minimax.bfs(board, 1, 1, 1)
# print(minimax.look_for_jump(board, 1, 1, 1))
# paths = minimax.start_move(board, 0, 1, 1)
# print(paths)
# boards = minimax.generate_boards_for_one_piece(board, paths)
# for board in boards:
#     game_utils.checkers.print_board(board)
#     print()

# boards = minimax.get_all_legal_boards(initial_board, 1)
# for board in boards:
#     print(f"score: {minimax.evaluate_board(initial_board, board, 1)}")
#     game_utils.checkers.print_board(board)
#     print()
board = minimax.get_best_move(initial_board, 1, depth=2)
board = np.rot90(board, 2)

game_utils.checkers.print_board(board)

# minimax.get_scores(initial_board, 1)
