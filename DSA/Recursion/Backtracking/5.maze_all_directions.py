# use recursion to find the paths for a obstacle maze
# Rules: you can move any direction
#  thinking processs:
# why cant i use the maze_right_down_diag_ret_paths.py with left and up direction calls?
# because if you add left and up, its going to be stuck in a loop like DUDUDUDUD.... so on
# to prevent this we must not travel the path already traversed. how to make it... make the cell false(obstacle creation) as soon as we pass it
# there is a problem.. how to revert this false back to true. because other recursion call may also land on the same cell.. after return call make the cell back to TRUE

def mazePaths(boolMaze):
    def pathFinder(boolMaze, row, col, pathCoord, res):
        # out of bounds, return
        if row > len(boolMaze) -1 or col > len(boolMaze[0])-1 or row < 0 or col < 0:
            return
        # check for osbtacles i.e false in the maze
        if boolMaze[row][col] == False:
            return
        # only append the paths if pos reaches the end
        if row == len(boolMaze) -1 and col == len(boolMaze[0])-1:
            res.append(pathCoord)
            return
        # we are in new cell mark it False
        boolMaze[row][col] = False # making the cell FALSE as soon we are passing to next cell
        
        # down direction  
        pathFinder(boolMaze, row+1, col, pathCoord+[ [row+1, col] ], res)
        # right direction
        pathFinder(boolMaze, row, col+1, pathCoord+[ [row, col+1] ], res)
        # left direction
        pathFinder(boolMaze, row, col-1, pathCoord+[ [row, col-1] ], res)
        # up direction  
        pathFinder(boolMaze, row-1, col, pathCoord+[ [row-1, col] ], res)
        # right direction
        pathFinder(boolMaze, row+1, col+1, pathCoord+[ [row+1, col+1] ], res)
        
        for ls in res: # just printing to understand the current res 
            print(ls)
        print("remarking the cell to true")
        # making the cell TRUE as soon we return from that recursion leg
        # all the possible answers have been found for this leg go back one call and try again with remaining possible soulutions
        #  if you are still confused you need to understand the recursion and its current stack memory go back and revise
        boolMaze[row][col] = True # making the cell TRUE as soon we return from that recursion leg

        
    res = []
    pathCoord = []
    row = 0
    col = 0
    pathFinder(boolMaze, row, col, pathCoord, res)
    return res


bool_maze = [ 
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
bool_maze = [ 
    [1, 1, 1],
    [1, 1, 1]
]

ans = mazePaths(bool_maze)

for ls in ans:
    print(ls)
print(len(ans))