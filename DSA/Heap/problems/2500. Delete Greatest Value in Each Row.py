def deleteGreatestValue(grid):
    for nums in grid:
        nums.sort()
    output = 0
    print(grid)

    while len(grid[0]) > 0:
        maxval = 0
        for i in range(len(grid)):
            maxval = max(maxval, grid[i].pop())
            print(grid)
            print(len(grid))
        
        output += maxval

    return output

grid = [[1,2,4],[3,3,1]]
print(deleteGreatestValue(grid))


import heapq

def deleteGreatestValue(self, grid) -> int:
    for i in range(len(grid)):
        heapq._heapify_max(grid[i])
    
    output = 0
    
    while len(grid[0]) > 0:
        maxval = 0
        for i in range(len(grid)):
            maxval = max(maxval, heapq._heappop_max(grid[i]))
        
        output += maxval
    
    return output