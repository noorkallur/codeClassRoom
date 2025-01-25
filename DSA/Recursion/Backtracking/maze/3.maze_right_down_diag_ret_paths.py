# use recursion to find the paths
# reduce the coordinates by 1(row, col and both) till you reach the destination each node will have three nodes again (possibly if the row ,col doesnot go over bounds)

def mazePaths(destCoord):
    def pathFinder(destCoord, currPos, pathCoord, res):
        if currPos[0] > destCoord[0] or currPos[1] > destCoord[1]:
            return
        if currPos[0] == destCoord[0] and currPos[1] == destCoord[1]:
            res.append(pathCoord)
            return
        
        # down direction  
        pathFinder(destCoord, [currPos[0]+1, currPos[1]], pathCoord+[ [currPos[0]+1, currPos[1]] ], res)
        # diagonal direction
        pathFinder(destCoord, [currPos[0]+1, currPos[1]+1], pathCoord+[ [currPos[0]+1, currPos[1]+1] ], res)
        # right direction
        pathFinder(destCoord, [currPos[0], currPos[1]+1], pathCoord+[ [currPos[0], currPos[1]+1] ], res)
        
    res = []
    pathCoord = []
    currPos = [0, 0]
    pathFinder(destCoord, currPos, pathCoord, res)
    return res

ans = mazePaths([2,1])
for ls in ans:
    print(ls)
print(len(ans))
