
import numpy as np

import game_utils


def get_best_move(initial_board, player, depth=1):
    boards = get_all_legal_boards(initial_board, player)
    scores = []
    for board in boards:
        if depth == 0:
            scores.append(evaluate_board(initial_board, board, player))
        else:
            opponent_best_move = get_opponent_best_move(board, player, depth)
            scores.append(evaluate_board(
                initial_board, opponent_best_move, player))
    best_score = max(scores)
    best_move = boards[scores.index(best_score)]
    return best_move


def get_opponent_best_move(initial_board, player, depth=1):
    boards = get_all_legal_boards(initial_board, -player)
    scores = []
    for board in boards:
        if depth == 0:
            scores.append(evaluate_board(initial_board, board, player))
        else:
            my_best_move = get_best_move(board, -player, depth - 1)
            scores.append(evaluate_board(initial_board, my_best_move, player))
    best_score = min(scores)
    best_move = boards[scores.index(best_score)]
    return best_move


def evaluate_board(intitial_board, new_board, player):
    player_pieces_initial = np.count_nonzero(intitial_board == player)
    player_pieces_new = np.count_nonzero(new_board == player)
    opponent_pieces_initial = np.count_nonzero(intitial_board == -player)
    opponent_pieces_new = np.count_nonzero(new_board == -player)
    return player_pieces_new - player_pieces_initial + opponent_pieces_initial - opponent_pieces_new


def get_all_legal_boards(board, player):
    boards = []

    if player == -1:
        # rotate board by 180 degrees
        board = np.rot90(board, 2)

    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            if board[y, x] == player:
                paths = start_move(board, y, x, player)
                boards = boards + \
                    generate_boards_for_one_piece(board, paths, player)

    if player == -1:
        # rotate board by 180 degrees
        boards = [np.rot90(board, 2) for board in boards]
    return boards


def generate_boards_for_one_piece(board, paths, player):
    boards = []
    for path in paths:
        if len(path) == 1:
            continue
        new_board = board.copy()
        for i in range(len(path) - 1):
            y = path[i][0]
            x = path[i][1]
            new_board[y][x] = 0
        y = path[-1][0]
        x = path[-1][1]
        new_board[y][x] = player
        boards.append(new_board)
    return boards


def start_move(board, y, x, player):
    # move left
    left_path = [[(y, x)]]
    if x - 1 >= 0 and y + 1 < board.shape[0]:
        first_jump = board[y + 1, x - 1]
        if first_jump == 0:
            left_path[0].append((y + 1, x - 1))
            # paths.append(left_path)
        elif first_jump == -player and x - 2 >= 0 and y + 2 < board.shape[0]:
            second_jump = board[y + 2, x - 2]
            if second_jump == 0:
                left_path[0].append((y + 1, x - 1))
                left_path[0].append((y + 2, x - 2))
                # paths.append(left_path)

    # move right
    right_path = [[(y, x)]]
    if x + 1 < board.shape[1] and y + 1 < board.shape[0]:
        first_jump = board[y + 1, x + 1]
        if first_jump == 0:
            right_path[0].append((y + 1, x + 1))
            # paths.append(right_path)
        elif first_jump == -player and x + 2 < board.shape[1] and y + 2 < board.shape[0]:
            second_jump = board[y + 2, x + 2]
            if second_jump == 0:
                right_path[0].append((y + 1, x + 1))
                right_path[0].append((y + 2, x + 2))
                # paths.append(right_path)

    if len(left_path[0]) == 3:
        left_path = look_for_jump(board, player, left_path)
    if len(right_path[0]) == 3:
        right_path = look_for_jump(board, player, right_path)

    # print(left_path)
    # print(right_path)
    paths = []
    # paths = paths + left_path + right_path
    for path in left_path:
        paths.append(path)
    for path in right_path:
        paths.append(path)
    return paths


def look_for_jump(board, player, paths=[[(0, 1), (1, 2), (2, 3)]]):
    # paths = [[(1, 1), (2, 2), (3, 3)]]
    # paths = [[(0, 1), (1, 2), (2, 3)]]
    new_paths = []
    for path in paths:
        # new_path = path
        last_coordinate = path[-1]
        y = last_coordinate[0]
        x = last_coordinate[1]
        # check if we can jump
        # can we move left
        changed = False
        if y + 2 < board.shape[0]:

            if x - 2 >= 0:
                first_jump = board[y + 1, x - 1]
                second_jump = board[y + 2, x - 2]
                if first_jump == -player and second_jump == 0:
                    new_path = path + [(y + 1, x - 1), (y + 2, x - 2)]
                    new_paths.append(new_path)
                    changed = True

            if x + 2 < board.shape[1]:
                first_jump = board[y + 1, x + 1]
                second_jump = board[y + 2, x + 2]
                if first_jump == -player and second_jump == 0:
                    new_path = path + [(y + 1, x + 1), (y + 2, x + 2)]
                    new_paths.append(new_path)
                    changed = True

        if not changed:
            new_paths.append(path)

    # print(new_paths)
    if new_paths == paths:
        return new_paths
    return look_for_jump(board, player, new_paths)
