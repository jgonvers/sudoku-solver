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
        return(count)
            
    def get_line(i ,j):
        return {x for x in board[i] if is_sol(x)}
    def get_column(i,j):
        return {x for x in [y[j] for y in board] if is_sol(x)}
    def get_square(i,j):
        square = set()
        pos_line = 3*(j//3)
        pos_col = 3*(i//3)
        for x in range(3):
            for y in range(3):
                if is_sol(board[y+pos_col][x+pos_line]):
                    square.add(board[y+pos_col][x+pos_line])
        return square
    
    def possibility(i,j):
        if is_sol(board[i][j]):
            return(board[i][j])
        pos = set(list("123456789"))-(get_line(i,j)|get_column(i,j)|get_square(i,j))
        if len(pos) == 1:
            return pos.pop()
        else:
            return pos
    
    def get_first(board):
        for i in range(9):
            for j in range(9):
                if type(board[i][j]) == set:
                    return(i, j, board[i][j])
    
    old_count = 0
    while(True):
        for i in range(9):
            for j in range(9):
                board[i][j] = possibility(i,j)
        count = count_sol(board)
        if old_count == count:
            new_board = board
            i,j,pos = get_first(new_board)
            print_board(new_board)
            for p in pos:
                new_board[i][j] = p
                sudoku_solve(new_board)
                print(count_sol(new_board))
                if count_sol(new_board) == 81:
                    break
            break
        else:
            old_count = count
        
        
    
        
def print_board(board, show_pos=False):
    for x in board:
        print(x)


board_easy = [list("....8.1.."),
              list(".43....76"),
              list("7.1..4..."),
              list("....567.9"),
              list("5...4..18"),
              list(".3...7..."),
              list(".6.9.8..."),
              list("3851.24.7"),
              list("9.74.5682")]

board = [["7","5","2",".","4",".",".","3","1"],
         [".","8",".",".",".","1",".",".","."],
         [".",".",".",".","2",".","5",".","9"],
         [".",".","7",".",".",".",".",".","."],
         ["2",".","8",".",".",".",".","5","."],
         ["6","9","1","7","5",".",".",".","."],
         [".",".",".","9",".",".",".",".","."],
         ["9","2",".",".","8",".",".","6","3"],
         [".","6","5",".",".","4",".","2","."]]

print_board(board_easy)
sudoku_solve(board_easy)
print_board(board_easy)