# https://leetcode.com/problems/sudoku-solver/description/
def is_num_valid(board, num, row, col):
    #horizontal line and verical line
    for itr in range(0, 9):
        # print(f"Horiz:{board[row][itr]}")
        if board[row][itr] == num or board[itr][col] == num:
            return False
    
    # box check
    if row < 3:
        row = 0
    elif row < 6:
        row = 3
    else:
        row = 6
    
    if col < 3:
        col = 0
    elif col < 6:
        col = 3
    else:
        col = 6
        
    for i in range(row, row+3):
        for j in range(col, col+3):
            # print(f"Ver:{board[i][j]}")
            if board[i][j] == num:
                return False
            
    return True
    
def dispboard(board):
        for row in board:
            print(" ".join(str(item) for item in row))
            print("")
            
def solver_engine(board, row, col):
    if row == 9:
        return True # if solution found, return true to stop iterations 
    
    if col == 9:
        return solver_engine(board, row+1, 0)        
    
    if board[row][col] == ".":
        for num in range(1,10):
            if is_num_valid(board, str(num), row, col):
                board[row][col] = str(num)
                if solver_engine(board, row, col+1): # if solution found, stop iterations
                    return True
                board[row][col] = "."
        return False
    
    return solver_engine(board, row, col+1)
        
        
def solveSudoku(board):
    row = 0
    col = 0
    solver_engine(board, row, col)
  
board = [
    ["5","3",".",  ".","7",".",  ".",".","."],
    ["6",".",".",  "1","9","5",  ".",".","."],
    [".","9","8",  ".",".",".",  ".","6","."],
    
    ["8",".",".",  ".","6",".",  ".",".","3"],
    ["4",".",".",  "8",".","3",  ".",".","1"],
    ["7",".",".",  ".","2",".",  ".",".","6"],
    
    [".","6",".",  ".",".",".",  "2","8","."],
    [".",".",".",  "4","1","9",  ".",".","5"],
    [".",".",".",  ".","8",".",  ".","7","9"]
    ]  


board = [[".",".",  ".",".",".",  ".",".",".","."],
         [".","9",  ".",".","1",  ".",".","3","."],
         [".",".",  "6",".","2",  ".","7",".","."],
         
         [".",".",  ".","3",".",  "4",".",".","."],
         ["2","1",  ".",".",".",  ".",".","9","8"],
         [".",".",  ".",".",".",  ".",".",".","."],
         
         [".",".",  "2","5",".",  "6","4",".","."],
         [".","8",  ".",".",".",  ".",".","1","."],
         [".",".",  ".",".",".",  ".",".",".","."]
        ]

solveSudoku(board)

dispboard(board)



#############################################################################################################
# Another way for is_num_valid

def is_num_valid(board, num, row, col):
    #horizontal line and verical line
    for itr in range(0, 9):
        # print(f"Horiz:{board[row][itr]}")
        if board[row][itr] == num or board[itr][col] == num:
            return False
    
    # box check
    row = row - row % 3
    col = col - col % 3
    print(f"row{row}, col{col}")
    for i in range(row, row+3):
        for j in range(col, col+3):
            # print(f"Ver:{board[i][j]}")
            if board[i][j] == num:
                return False
            
    return True

is_num_valid(board, 4, 4 ,1)
