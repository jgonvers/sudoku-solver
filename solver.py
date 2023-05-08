def sudoku_solve(board):
    def is_sol(x):
        if type(x) != str:
            return False
        return x in "123456789"

    def count_sol(board):
        count = 0
        for line in board:
            for case in line:
                if is_sol(case):
                    count += 1
        return count

    def get_line(i, j):
        return {x for x in board[i] if is_sol(x)}

    def get_column(i, j):
        return {x for x in [y[j] for y in board] if is_sol(x)}

    def get_square(i, j):
        square = set()
        pos_line = 3 * (j // 3)
        pos_col = 3 * (i // 3)
        for x in range(3):
            for y in range(3):
                if is_sol(board[y + pos_col][x + pos_line]):
                    square.add(board[y + pos_col][x + pos_line])
        return square

    def possibility(i, j):
        if is_sol(board[i][j]):
            return board[i][j]
        pos = set(list("123456789")) - (
            get_line(i, j) | get_column(i, j) | get_square(i, j)
        )
        return pos

    def get_first(board):
        for i in range(9):
            for j in range(9):
                if type(board[i][j]) == set:
                    return (i, j, board[i][j])

    def fill_board(board):
        old_count = 0
        count = -1
        while count != old_count:
            old_count = count
            for i in range(9):
                for j in range(9):
                    pos = possibility(i, j)
                    if len(pos) == 0:
                        board[i][j] = pos
                        return False
                    elif len(pos) == 1 and type(pos) != str:
                        board[i][j] = pos.pop()
                    else:
                        board[i][j] = pos
            count = count_sol(board)
        return True

    def copy_board(board):
        return [line.copy() for line in board]

    def copy_board2(b1, b2):
        for i in range(9):
            for j in range(9):
                b1[i][j] = b2[i][j]

    if fill_board(board):
        if count_sol(board) == 81:
            return True
        i, j, pos = get_first(board)
        for p in pos:
            new_board = copy_board(board)
            new_board[i][j] = p
            if sudoku_solve(new_board):
                copy_board2(board, new_board)
                return True
        return False

    else:
        return False


board_easy = [
    list("....8.1.."),
    list(".43....76"),
    list("7.1..4..."),
    list("....567.9"),
    list("5...4..18"),
    list(".3...7..."),
    list(".6.9.8..."),
    list("3851.24.7"),
    list("9.74.5682"),
]

board = [
    list(".268..3.."),
    list(".5......6"),
    list(".73.65.9."),
    list("...74...8"),
    list("7.4...1.2"),
    list(".8...3.79"),
    list("1.....2.4"),
    list("..29....."),
    list(".6.47...."),
]


def print_board(board):
    for line in board:
        print(line)


print_board(board)
print()
sudoku_solve(board)
print()
print_board(board)
