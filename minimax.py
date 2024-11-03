
import numpy as np

import game_utils

# TODO implement game ending when there are no pieces
# TODO only allow jumping when there is a jump available


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
    player_kings_initial = np.count_nonzero(intitial_board == player * 2)
    player_kings_new = np.count_nonzero(new_board == player * 2)
    opponent_pieces_initial = np.count_nonzero(intitial_board == -player)
    opponent_pieces_new = np.count_nonzero(new_board == -player)
    opponent_kings_initial = np.count_nonzero(intitial_board == -player * 2)
    opponent_kings_new = np.count_nonzero(new_board == -player * 2)
    score = 0
    score += (player_pieces_new - player_pieces_initial) * 1
    score += (player_kings_new - player_kings_initial) * 2
    score += (opponent_pieces_new - opponent_pieces_initial) * -1
    score += (opponent_kings_new - opponent_kings_initial) * -2
    return score


def get_all_legal_boards(board, player):
    boards = []

    if player == -1:
        # rotate board by 180 degrees
        board = np.rot90(board, 2)

    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            piece = board[y, x]
            if piece == player or piece == player * 2:
                is_king = piece == player * 2
                paths = start_move(board, y, x, player, is_king)
                boards = boards + \
                    generate_boards_for_one_piece(
                        board, paths, player, is_king)

    if player == -1:
        # rotate board by 180 degrees
        boards = [np.rot90(board, 2) for board in boards]

    # for board in boards:
    #     game_utils.checkers.print_board(board)
    #     print()
    return boards


def generate_boards_for_one_piece(board, paths, player, is_king):
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
        piece = player
        if is_king or (not is_king and y == board.shape[0] - 1):
            piece = piece * 2
        new_board[y][x] = piece
        boards.append(new_board)
    return boards


def start_move(board, y, x, player, is_king):
    # move left
    lower_left_path = [[(y, x)]]
    if x - 1 >= 0 and y + 1 < board.shape[0]:
        first_jump = board[y + 1, x - 1]
        if first_jump == 0:
            lower_left_path[0].append((y + 1, x - 1))
            # paths.append(left_path)
        elif (first_jump == -player or first_jump == 2 * - player) and x - 2 >= 0 and y + 2 < board.shape[0]:
            second_jump = board[y + 2, x - 2]
            if second_jump == 0:
                lower_left_path[0].append((y + 1, x - 1))
                lower_left_path[0].append((y + 2, x - 2))
                # paths.append(left_path)

    # move right
    lower_right_path = [[(y, x)]]
    if x + 1 < board.shape[1] and y + 1 < board.shape[0]:
        first_jump = board[y + 1, x + 1]
        if first_jump == 0:
            lower_right_path[0].append((y + 1, x + 1))
            # paths.append(right_path)
        elif (first_jump == -player or first_jump == 2 * - player) and x + 2 < board.shape[1] and y + 2 < board.shape[0]:
            second_jump = board[y + 2, x + 2]
            if second_jump == 0:
                lower_right_path[0].append((y + 1, x + 1))
                lower_right_path[0].append((y + 2, x + 2))
                # paths.append(right_path)

    upper_left_path = []
    upper_right_path = []
    if is_king:
        upper_left_path = [[(y, x)]]
        if x - 1 >= 0 and y - 1 >= 0:
            first_jump = board[y - 1, x - 1]
            if first_jump == 0:
                upper_left_path[0].append((y - 1, x - 1))
                # paths.append(left_path)
            elif (first_jump == -player or first_jump == 2 * - player) and x - 2 >= 0 and y - 2 >= 0:
                second_jump = board[y - 2, x - 2]
                if second_jump == 0:
                    upper_left_path[0].append((y - 1, x - 1))
                    upper_left_path[0].append((y - 2, x - 2))
                    # paths.append(left_path)

        upper_right_path = [[(y, x)]]
        if x + 1 < board.shape[1] and y - 1 >= 0:
            first_jump = board[y - 1, x + 1]
            if first_jump == 0:
                upper_right_path[0].append((y - 1, x + 1))
                # paths.append(right_path)
            elif (first_jump == -player or first_jump == 2 * - player) and x + 2 < board.shape[1] and y - 2 >= 0:
                second_jump = board[y - 2, x + 2]
                if second_jump == 0:
                    upper_right_path[0].append((y - 1, x + 1))
                    upper_right_path[0].append((y - 2, x + 2))
                    # paths.append(right_path)

    if len(lower_left_path[0]) == 3:
        lower_left_path = look_for_jump(board, player, lower_left_path)
    if len(lower_right_path[0]) == 3:
        lower_right_path = look_for_jump(board, player, lower_right_path)
    if is_king:
        if len(upper_left_path[0]) == 3:
            upper_left_path = look_for_jump(board, player, upper_left_path)
        if len(upper_right_path[0]) == 3:
            upper_right_path = look_for_jump(board, player, upper_right_path)

    # print(left_path)
    # print(right_path)
    paths = []
    # paths = paths + left_path + right_path
    for path in lower_left_path:
        paths.append(path)
    for path in lower_right_path:
        paths.append(path)
    for path in upper_left_path:
        paths.append(path)
    for path in upper_right_path:
        paths.append(path)
    return paths


def look_for_jump(board, player, paths=[], is_king=False):
    """
    Check if we can jump over multiple opponent pieces in one move.

    Returns a list of paths.
    """
    new_paths = []
    for path in paths:
        last_coordinate = path[-1]
        y = last_coordinate[0]
        x = last_coordinate[1]
        changed = False

        first_coordinate_y = []
        first_coordinate_x = []
        second_coordinate_y = []
        second_coordinate_x = []
        if is_king and y - 2 >= 0:
            first_coordinate_y.append(y - 1)
            second_coordinate_y.append(y - 2)

        if y + 2 < board.shape[0]:
            first_coordinate_y.append(y + 1)
            second_coordinate_y.append(y + 2)

        if x - 2 >= 0:
            first_coordinate_x.append(x - 1)
            second_coordinate_x.append(x - 2)

        if x + 2 < board.shape[1]:
            first_coordinate_x.append(x + 1)
            second_coordinate_x.append(x + 2)

        for y_index in range(len(first_coordinate_y)):
            for x_index in range(len(first_coordinate_x)):
                new_path = get_jump_path_if_possible(first_coordinate=(first_coordinate_y[y_index], first_coordinate_x[x_index]),
                                                     second_coordinate=(second_coordinate_y[y_index], second_coordinate_x[x_index]), board=board, player=player)
                if new_path:
                    new_paths.append(path + new_path)
                    changed = True

        if not changed:
            new_paths.append(path)

    if new_paths == paths:
        return new_paths
    return look_for_jump(board=board, player=player, paths=new_paths, is_king=is_king)


def get_jump_path_if_possible(first_coordinate, second_coordinate, board, player):
    """
    Check if first coordinate is an opponent piece and second coordinate is empty.

    Returns `None` if jump isn't possible, if is possible, returns a list of coordinates the jump passes.
    """
    first_key = board[first_coordinate[0], first_coordinate[1]]
    second_key = board[second_coordinate[0], second_coordinate[1]]
    if (first_key == -player or first_key == 2 * - player) and second_key == 0:
        return [first_coordinate, second_coordinate]
    return None
