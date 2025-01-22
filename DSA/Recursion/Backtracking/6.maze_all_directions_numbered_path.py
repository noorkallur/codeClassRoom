# use recursion to find all the paths for a maze
# Rules: you can move any direction
# print the path in the matrix form using numbers for all the possible solution one such soln is 
    # [1, 0, 0],
    # [2, 0, 0],
    # [3, 4, 5]
# return a list of these numbered paths 
# if the question is still vague check the quesiton from the link below
# https://youtu.be/zg5v2rlV1tM?si=1x1VuOYjfPDLk3Im&t=4483
def mazePaths(maze):
    def pathFinder(maze, row, col, count, res):
        if row < 0 or col < 0 or row > len(maze)-1 or col > len(maze[0]) -1:
            return

        if maze[row][col] > 0:
            return
        
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            maze[row][col] = count
            # res.append(maze) # this cant be done because the maze is mutable and in the end its going to messed up as the refernce is same
            # deep copy manually
            sol_path = []
            for m in maze:
                print(m)
                sol_path.append(m[:])
            print("#######")
            res.append(sol_path)
            maze[row][col] = 0
            return
        
        # increment this cell with step count
        maze[row][col] = count
        # right
        pathFinder(maze, row, col+1, count+1, res)
        pathFinder(maze, row, col-1, count+1, res)
        pathFinder(maze, row+1, col+1, count+1, res)
        pathFinder(maze, row+1, col, count+1, res)
        pathFinder(maze, row-1, col, count+1, res)
        
        maze[row][col] = 0
        
    
    row = 0
    col = 0 
    res = []
    count = 1
    
    pathFinder(maze, row, col, count, res)
    
    return res   


bool_maze = [ 
    [0, 0, 0],
    [0, 0, 0]
]
bool_maze = [ 
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

ans = mazePaths(bool_maze)

for ls in ans:
    print(ls)
print(len(ans))
    