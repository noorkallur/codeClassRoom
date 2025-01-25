# Find the total number of ways you can place N knights in N X N board
total_iterations = 0

def isKnightSafe(board, row, col):
    global total_iterations
    total_iterations += 1  # counting the iterations just to see how many times it entered this func
    # only 4 positions above the knight 
    # pos1
    if row-2 >= 0 and col+1 < len(board[0]) and board[row-2][col+1] == 1:
        return False 
    # pos2
    if row-2 >= 0 and col-1 >= 0 and board[row-2][col-1] == 1:
        return False
    # pos3
    if row-1 >= 0 and col+2 < len(board[0]) and board[row-1][col+2] == 1:
        return False
    # pos4
    if row-1 >= 0 and col-2 >= 0 and board[row-1][col-2] == 1:
        return False
    
    return True

# def isKnightSafe(board, row, col):
#     global total_iterations
#     total_iterations += 1  # counting the iterations just to see how many times it entered this func
#     # Check only the 4 positions above the knight
#     knight_moves = [(-2, 1), (-2, -1), (-1, 2), (-1, -2)]
#     for move in knight_moves:
#         new_row, new_col = row + move[0], col + move[1]
#         if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 1:
#             return False
#     return True

def displayBoard(board):
    for row_ls in board:
        # print( f"{" ".join(str(item)) for item in row_ls}" )
        print(" ".join(str(item) for item in row_ls))
    print("")
        
def counter(board, row, col, knightCount):
    if knightCount == len(board[0]):
        displayBoard(board)
        return 1
    
    if row >= len(board): # to stop if we go out of the board
        return 0
    
    total_solutions = 0 # to keep track of the no of solutions
    
    if col == len(board[0]): # this is the tricky part, once we are out of col bounds, we reset the col count and proceed with next row
        total_solutions+=counter(board, row+1, 0, knightCount)
        return total_solutions 
    
    if isKnightSafe(board, row, col):
        board[row][col] = 1
        total_solutions+=counter(board, row, col+1, knightCount+1) # we place the knight and move ahead to next col
        board[row][col] = 0
    
    total_solutions+=counter(board, row, col+1, knightCount) # we dont place the knight and move ahead to next col
    
    return total_solutions # this will return for each leg
    

def nKnights(N):
    #creating board
    board = [[0 for _ in range(N)] for _ in range(N) ]
    row = 0
    col = 0
    knightCount = 0
    return counter(board, row, col, knightCount)

print(nKnights(3))
print(f"total iterations:{total_iterations}")
    
