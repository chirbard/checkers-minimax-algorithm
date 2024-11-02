class checkers:
    _print_keys = {
        0: '| ',
        1: '|x',
        -1: '|o',
    }

    @staticmethod
    def print_board(board):
        for column_index in range(board.shape[0]):
            for row_index in range(board.shape[1]):
                print(
                    checkers._print_keys[board[column_index, row_index]], end='')
            print('|')
