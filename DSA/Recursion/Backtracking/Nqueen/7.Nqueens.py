# Return the number of ways you can place a queen in NxN chess board without attacking eachother
# Rule: you have to place the one queen in all of the rows
# For example there are 0 ways to place queen(one in each row) in 3 x 3 board
# For example there are 2 ways to place queen(one in each row) in 4 x 4 board
# Look at the diagram in nqueens_refernce.png
##########################################################################################################
def isQueenSafe(board, row, col):
    # veritcal cell attack check
    for i in range(1, row+1):
        if board[row - i][col]:
            return False
        
    # left diagonal attack check
    # To calculate diagonal length : its mathematically min(row, col)
    diagLen = min(row, col)
    for i in range(1,  diagLen+1): # starting from 1 to diag length inclusive hence +1
        if board[row -i][col -i]:
            return False
    
    # right diagonal attack check
    # To calculate diagonal length : its mathematically min(row, len(col) - col) since its 0 index the actual is min(row, len(col)-1 - col) 
    diagLen = min(row, (len(board[0])-1 -col))
    for i in range(1,  diagLen +1): # starting from 1 to diag length inclusive hence +1
        if board[row -i][col +i]:
            return False
    
    return True

def displayBoard(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print("") # new line
    
def countSoultions(board, row):
    # when in the last row, means we found one possible solution
    if row >= len(board):
        displayBoard(board)
        return 1
    
    count = 0 # to count the no of ways
    for col in range(0, len(board[0])):
        if isQueenSafe(board, row, col): # before placing queen(1) check if its safe in the position
            board[row][col] = 1
            count += countSoultions(board, row+1) # counting recursively
            board[row][col] = 0
    
    return count  # this only be hit once, at the end

def Nqueen(nrows, ncols):          
    board =[[0 for _ in range(ncols)] for _ in range(nrows)]
    row = 0
    return countSoultions(board, row) # helper funtion to insert board and inital row positon
    
print(Nqueen(8, 8)) # 92 ways
print(Nqueen(4, 4)) # 2  ways
# Time complexity is pretty interesting here please take a look at the image first nqueen_q_arrangements.png first 
