# use recursion to find the paths for a obstacle maze(false being obstacle)
# Rules: 
# 1.person starts at 0,0 
# 2.can only moce Right direction  or Down direction one step at a time
# Thinking process:
# goal is to end end of the maze
# reduce the coordinates by 1(row, col) till you reach the end of the maze
# since its a bool maze false being the obstacle check every time and return from that recursion 

def mazePaths(boolMaze):
    def pathFinder(boolMaze, row, col, pathCoord, res):
        # out of bounds, return
        if row > len(boolMaze) -1 or col > len(boolMaze[0])-1:
            return
        # check for osbtacles i.e false in the maze
        if boolMaze[row][col] == False:
            return
        # only append the paths if pos reaches the end
        if row == len(boolMaze) -1 and col == len(boolMaze[0])-1:
            res.append(pathCoord)
            return
        
        # down direction  
        pathFinder(boolMaze, row+1, col, pathCoord+[ [row+1, col] ], res)
        # right direction
        pathFinder(boolMaze, row, col+1, pathCoord+[ [row, col+1] ], res)
        
    res = []
    pathCoord = []
    row = 0
    col = 0
    pathFinder(boolMaze, row, col, pathCoord, res)
    return res


bool_maze = [ 
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
] # [[1, 0], [2, 0], [2, 1], [2, 2]] [[0, 1], [0, 2], [1, 2], [2, 2]]

bool_maze = [ 
    [1, 1, 1],
    [0, 1, 1],
    [1, 1, 1]
] #[[0, 1], [1, 1], [2, 1], [2, 2] [[0, 1], [1, 1], [1, 2], [2, 2]] [[0, 1], [0, 2], [1, 2], [2, 2]]

bool_maze = [ 
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 0]
] # None

bool_maze = [ 
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1]
] # None

bool_maze = [ 
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
] # [[0, 1], [0, 2], [1, 2], [2, 2]]

ans = mazePaths(bool_maze)

for ls in ans:
    print(ls)
print(len(ans))
