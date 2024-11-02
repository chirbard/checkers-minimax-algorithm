
def get_best_move(board, depth=3):
    pass


def get_all_legal_moves(board, player):
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            if board[y, x] == player:
                possible_moves = get_bottom_moves(board, y, x, player)
                for move in possible_moves:
                    if move:
                        look_for_opponent(board, move, player)
                print(possible_moves)


def bfs(board, y, x, player, coordinates_to_visit=[]):
    # coordinates: (y, x, direction)
    # if direction is 0 this means we are starting moving
    # if direction is 1 we only look for moves to right
    # if direction is -1 we only look for moves to left

    coordinates_to_visit = [(y, x, 0)]
    while coordinates_to_visit:
        print(f"coordinates to visit: {coordinates_to_visit}")
        coordinates = coordinates_to_visit.pop(0)
        y = coordinates[0]
        x = coordinates[1]
        direction = coordinates[2]

        current_piece = player
        try:
            current_piece = board[y, x]
        except IndexError:
            pass

        if direction == 0:
            new_coordinates = [(y + 1, x - 1, -1), (y + 1, x + 1, 1)]
            coordinates_to_visit = coordinates_to_visit + new_coordinates
            continue

        if current_piece == 0 and direction != 0:
            print(f"possible end position: {y, x}")
            continue

        # print(f"current piece: {current_piece}")
        # print(f"coordinates: {y, x}")
        # print(f"direction: {direction}")
        # print()

        if current_piece == -player:
            new_x = x + direction
            new_y = y + 1
            new_direction = 0
            new_piece = player
            try:
                new_piece = board[new_y, new_x]
            except IndexError:
                pass
            if new_piece == 0:
                # print(f"new coordinates: {new_y, new_x, new_direction}")
                coordinates_to_visit.append((new_y, new_x, new_direction))

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
