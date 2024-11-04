
import numpy as np


class Minimax:
    @staticmethod
    def get_best_move(initial_board, player, depth=1):
        """
        Returns the best move as a new board(matrix).
        """
        boards = Minimax.__get_all_legal_boards(initial_board, player)
        scores = []
        for board in boards:
            if depth == 0:
                scores.append(Minimax.__evaluate_board(
                    initial_board, board, player))
            else:
                opponent_best_move = Minimax.__get_opponent_best_move(
                    board, player, depth)
                scores.append(Minimax.__evaluate_board(
                    initial_board, opponent_best_move, player))
        best_score = max(scores)
        best_move = boards[scores.index(best_score)]
        return best_move

    @staticmethod
    def __get_opponent_best_move(initial_board, player, depth=1):
        """
        Returns opponent's best move as a new board(matrix).
        """
        boards = Minimax.__get_all_legal_boards(initial_board, -player)
        scores = []
        for board in boards:
            if depth == 0:
                scores.append(Minimax.__evaluate_board(
                    initial_board, board, player))
            else:
                my_best_move = Minimax.get_best_move(board, -player, depth - 1)
                scores.append(Minimax.__evaluate_board(
                    initial_board, my_best_move, player))
        best_score = min(scores)
        best_move = boards[scores.index(best_score)]
        return best_move

    @staticmethod
    def __evaluate_board(intitial_board, new_board, player):
        """
        Returns a score for a board(matrix) based on the difference in number of pieces and kings.
        """
        player_pieces_initial = np.count_nonzero(intitial_board == player)
        player_pieces_new = np.count_nonzero(new_board == player)
        player_kings_initial = np.count_nonzero(intitial_board == player * 2)
        player_kings_new = np.count_nonzero(new_board == player * 2)
        opponent_pieces_initial = np.count_nonzero(intitial_board == -player)
        opponent_pieces_new = np.count_nonzero(new_board == -player)
        opponent_kings_initial = np.count_nonzero(
            intitial_board == -player * 2)
        opponent_kings_new = np.count_nonzero(new_board == -player * 2)
        score = 0
        score += (player_pieces_new - player_pieces_initial) * 1
        score += (player_kings_new - player_kings_initial) * 2
        score += (opponent_pieces_new - opponent_pieces_initial) * -1
        score += (opponent_kings_new - opponent_kings_initial) * -2
        return score

    @staticmethod
    def __get_all_legal_boards(board, player):
        """
        Returns a list of all possible boards(matrixes) after one move.
        """
        # TODO if a jump is possible discard non-jump moves
        boards = []

        if player == -1:
            board = np.rot90(board, 2)

        for y in range(board.shape[0]):
            for x in range(board.shape[1]):
                piece = board[y, x]
                if piece == player or piece == player * 2:
                    is_king = piece == player * 2
                    paths = Minimax.__start_move(board, y, x, player, is_king)
                    boards = boards + \
                        Minimax.__generate_boards_for_one_piece(
                            board, paths, player, is_king)

        if player == -1:
            boards = [np.rot90(board, 2) for board in boards]

        return boards

    @staticmethod
    def __generate_boards_for_one_piece(board, paths, player, is_king):
        """
        Generate a board(matrix) from path(list of moves).

        Returns a list of boards(matrixes).
        """
        boards = []
        for path in paths:
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

    @staticmethod
    def __start_move(board, y, x, player, is_king):
        """
        Find all possible paths for a piece to move.

        Returns all possible paths for a piece to move.
        """
        lower_left_paths = Minimax.__get_paths_in_one_direction((y, x),
                                                                (y + 1, x - 1), (y + 2, x - 2), board, player)
        lower_right_paths = Minimax.__get_paths_in_one_direction((y, x),
                                                                 (y + 1, x + 1), (y + 2, x + 2), board, player)

        upper_left_paths = []
        upper_right_paths = []
        if is_king:
            upper_left_paths = Minimax.__get_paths_in_one_direction((y, x),
                                                                    (y - 1, x - 1), (y - 2, x - 2), board, player)
            upper_right_paths = Minimax.__get_paths_in_one_direction((y, x),
                                                                     (y - 1, x + 1), (y - 2, x + 2), board, player)

        paths = []
        for path in lower_left_paths:
            paths.append(path)
        for path in lower_right_paths:
            paths.append(path)
        for path in upper_left_paths:
            paths.append(path)
        for path in upper_right_paths:
            paths.append(path)
        return paths

    @staticmethod
    def __get_paths_in_one_direction(initial_coordinate, first_coordinate, second_coordinate, board, player):
        """
        Generates all paths that can be taken in one direction.

        Returns a list of paths.
        """
        paths = [[]]
        is_first_y_valid = first_coordinate[0] >= 0 and first_coordinate[0] < board.shape[0]
        is_first_x_valid = first_coordinate[1] >= 0 and first_coordinate[1] < board.shape[1]
        if is_first_y_valid and is_first_x_valid:
            first_key = board[first_coordinate[0], first_coordinate[1]]
            if first_key == 0:
                paths[0].append(initial_coordinate)
                paths[0].append(first_coordinate)
                return paths

            is_second_y_valid = second_coordinate[0] >= 0 and second_coordinate[0] < board.shape[0]
            is_second_x_valid = second_coordinate[1] >= 0 and second_coordinate[1] < board.shape[1]
            if is_second_y_valid and is_second_x_valid and (first_key == -player or first_key == 2 * - player):
                second_key = board[second_coordinate[0], second_coordinate[1]]
                if second_key == 0:
                    paths[0].append(initial_coordinate)
                    paths[0].append(first_coordinate)
                    paths[0].append(second_coordinate)
                    paths = Minimax.__look_for_multiple_jumps(
                        board, player, paths=paths)
        if paths == [[]]:
            return []
        return paths

    @staticmethod
    def __look_for_multiple_jumps(board, player, paths=[], is_king=False):
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
                    new_path = Minimax.__get_jump_path_if_possible(first_coordinate=(first_coordinate_y[y_index], first_coordinate_x[x_index]),
                                                                   second_coordinate=(second_coordinate_y[y_index], second_coordinate_x[x_index]), board=board, player=player)
                    if new_path:
                        new_paths.append(path + new_path)
                        changed = True

            if not changed:
                new_paths.append(path)

        if new_paths == paths:
            return new_paths
        return Minimax.__look_for_multiple_jumps(board=board, player=player, paths=new_paths, is_king=is_king)

    @staticmethod
    def __get_jump_path_if_possible(first_coordinate, second_coordinate, board, player):
        """
        Check if first coordinate is an opponent piece and second coordinate is empty.

        Returns `None` if jump isn't possible, if is possible, returns a list of coordinates the jump passes.
        """
        first_key = board[first_coordinate[0], first_coordinate[1]]
        second_key = board[second_coordinate[0], second_coordinate[1]]
        if (first_key == -player or first_key == 2 * - player) and second_key == 0:
            return [first_coordinate, second_coordinate]
        return None
