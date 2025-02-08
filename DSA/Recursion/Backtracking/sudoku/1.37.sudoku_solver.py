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
            # print("")
            
# we are iterating through every col and if we find empty col then we start placing numbers one by one
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

# i found another solution which i feel like is more intuitive and better to understand check below 
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
def is_num_valid2(board, num, row, col):
    #horizontal line and verical line
    for itr in range(0, 9):
        # print(f"Horiz:{board[row][itr]}")
        if board[row][itr] == num or board[itr][col] == num:
            return False
    
    #box check
    row = row - row % 3 # row - modulus of the root(9) gives the index of the box start
    col = col - col % 3
    # print(f"row{row}, col{col}")
    for i in range(row, row+3):
        for j in range(col, col+3):
            # print(f"Ver:{board[i][j]}")
            if board[i][j] == num:
                return False
            
    return True


# finds the first empty cell in the sudoku
def find_empty_cell(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                return row, col
    return -1, -1
  
def solveSudoku2(board):
    row, col = find_empty_cell(board)
    
    if row == -1:
        return True # stop as soon as we hit this so as to preserve the board contents
    
    for num in range(1,10):
        if is_num_valid2(board, str(num), row, col):
            board[row][col] = str(num)
            solveSudoku2(board)
            board[row][col] = "."
            
    return False # if the anwer is not possible, this will hit
    
solveSudoku2(board)
print("new answer")
dispboard(board)



####################################
# revisited the same quesiton again
def isNumValid(num, row, col):
    if str(num) in board[row]:
        return False
    
    for r in range(len(board)):
        if str(num) == board[r][col]:
            return False
    
    row = row//3 * 3   
    col = col//3 * 3
    for r in range(row, row+3):
        for c in range(col, col+3):
            if str(num) == board[r][c]:
                return False
    
    return True
    

def dispboard(board):
    for b in board:
        print(b)
    print("")
    
    
def sudoku(board):
    
    def solverEngine(row, col):
        
        if row == len(board):
            dispboard(board)
            return
        
        if col == len(board[0]):
            solverEngine(row+1, 0)
            return
        
        if board[row][col] == ".":
            for num in range(1,10):
                if isNumValid(num, row, col):
                    board[row][col] = str(num)
                    solverEngine(row, col+1)
                    board[row][col] = "."
        else:
            solverEngine(row, col+1)
            
    solverEngine(0,0)