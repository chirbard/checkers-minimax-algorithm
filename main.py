import minimax
import game_utils
import numpy as np

# board = [
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [-1, 0, -1, 0, -1, 0],
#     [0, -1, 0, -1, 0, -1],
# ]

# board = [
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1],
#     [0, 0, -1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [-1, 0, -1, 0, -1, 0],
#     [0, 0, 0, -1, 0, 0],
# ]

board = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0],

]

board = np.array(board)
game_utils.checkers.print_board(board)

# minimax.get_all_legal_moves(board, 1)
# minimax.bfs(board, 1, 1, 1)
# print(minimax.look_for_jump(board, 1, 1, 1))
paths = minimax.start_move(board, 0, 1, 1)
print(paths)
boards = minimax.generate_boards_for_one_piece(board, paths)
for board in boards:
    game_utils.checkers.print_board(board)
    print()
