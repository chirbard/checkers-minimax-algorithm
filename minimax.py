
import numpy as np


def get_best_move(board, depth=3):
    pass


# def get_all_legal_moves(board, player):
#     for y in range(board.shape[0]):
#         for x in range(board.shape[1]):
#             if board[y, x] == player:
#                 possible_moves = get_bottom_moves(board, y, x, player)
#                 for move in possible_moves:
#                     if move:
#                         look_for_opponent(board, move, player)
#                 print(possible_moves)


# function look
# function look for empty which returns a list of all possible empty  to move to
# function look for jumps return list of moved coordinates. if we make multiple jumps then return the whole path recursively
#   note the path could branch out

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


# def bfs(board, y, x, player, coordinates_to_visit=[]):
#     # coordinates: (y, x, direction)
#     # if direction is 0 this means we are starting moving
#     # if direction is 1 we only look for moves to right
#     # if direction is -1 we only look for moves to left

#     coordinates_to_visit = [(y, x, 0)]
#     while coordinates_to_visit:
#         print(f"coordinates to visit: {coordinates_to_visit}")
#         coordinates = coordinates_to_visit.pop(0)
#         y = coordinates[0]
#         x = coordinates[1]
#         direction = coordinates[2]

#         current_piece = player
#         try:
#             current_piece = board[y, x]
#         except IndexError:
#             pass

#         if direction == 0:
#             new_coordinates = [(y + 1, x - 1, -1), (y + 1, x + 1, 1)]
#             coordinates_to_visit = coordinates_to_visit + new_coordinates
#             continue

#         if current_piece == 0 and direction != 0:
#             print(f"possible end position: {y, x}")
#             continue

#         # print(f"current piece: {current_piece}")
#         # print(f"coordinates: {y, x}")
#         # print(f"direction: {direction}")
#         # print()

#         if current_piece == -player:
#             new_x = x + direction
#             new_y = y + 1
#             new_direction = 0
#             new_piece = player
#             try:
#                 new_piece = board[new_y, new_x]
#             except IndexError:
#                 pass
#             if new_piece == 0:
#                 # print(f"new coordinates: {new_y, new_x, new_direction}")
#                 coordinates_to_visit.append((new_y, new_x, new_direction))

    # coordinates = coordinates_to_visit[0]
    # coordinates_to_visit = coordinates_to_visit[1:]
    # y = coordinates[0]
    # x = coordinates[1]
    # will_look_forward = coordinates[2]
    # current_piece = player
    # try:
    #     current_piece = board[y, x]
    # except IndexError:
    #     pass
    # if current_piece == player and not will_look_forward:
    #     continue

    # if current_piece == 0:
    #     # our piece can end here
    #     # so add this coordinate to the tree and return it
    #     # longest_tree.append((y, x))
    #     # return longest_tree
    #     print(f"possible end position: {y, x}")
    #     continue

    # if current_piece == player:
    #     new_coordinates = [(y + 1, x - 1, 0), (y + 1, x + 1, 0)]
    #     coordinates_to_visit = coordinates_to_visit + new_coordinates

    #     print(f"cooridnates now {coordinates_to_visit}")
    #     continue

    # if current_piece == -player:
    #     new_coordinates = [(y + 1, x - 1, 1), (y + 1, x + 1, 1)]
    #     coordinates_to_visit = coordinates_to_visit + new_coordinates
    #     print(f"cooridnates now {coordinates_to_visit}")
    #     continue

    # if current_piece == -player:
    #     # look for possible moves
    #     # coordinates_to_visit.append((y + 1, x - 1))
    #     # coordinates_to_visit.append((y + 1, x + 1))
    #     new_coordinates = [(y + 1, x - 1), (y + 1, x + 1)]
    #     bfs(board, y, x, player, new_coordinates)


# def look_for_opponent(board, move, player):
#     if move['key'] == -player:
#         possible_moves = get_bottom_moves(board, move['y'], move['x'], player)
#         print(f"opponent: {possible_moves}")


# def get_bottom_moves(board, y, x, player):
#     bottom_left = get_bottom_left(board, y, x, player)
#     bottom_right = get_bottom_right(board, y, x, player)
#     return [bottom_left, bottom_right]


# def get_bottom_left(board, y, x, player):
#     x = x - 1
#     y = y + 1
#     if x < 0:
#         return None

#     try:
#         key = board[y, x]
#         if key == player:
#             return None
#         return {
#             'key': key,
#             'y': y,
#             'x': x,
#         }
#     except IndexError:
#         return None


# def get_bottom_right(board, y, x, player):
#     x = x + 1
#     y = y + 1
#     if x < 0:
#         return None
#     try:
#         key = board[y, x]
#         if key == player:
#             return None
#         return {
#             'key': key,
#             'y': y,
#             'x': x,
#         }
#     except IndexError:
#         return None
