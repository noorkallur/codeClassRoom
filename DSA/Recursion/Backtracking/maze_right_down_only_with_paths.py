# please read and do the question maze_right_down_only_coun.py before as this is a subset of that quesiton.
#  now return the paths took to reach the destination coordinate
def mazePathCount(destCoordinates):
    def counter(destCoordinates, currPos, pathStr, res):
        if currPos[0] > destCoordinates[0] or currPos[1] > destCoordinates[1]: 
            return
        if currPos[0] == destCoordinates[0] and currPos[1] == destCoordinates[1]: 
            res.append(pathStr)
            return 
        
        # recursion logic; important how we pass params as the pathStr at this iteration is pathStr and we pass +D to next
        counter(destCoordinates, [currPos[0]+1,currPos[1]], pathStr+"D", res)
        counter(destCoordinates, [currPos[0],currPos[1]+1], pathStr+"R", res)
    
    currPos = [0,0]
    res = []
    pathStr = ""
    counter(destCoordinates, currPos, pathStr, res)
    return res

print(mazePathCount([2,2]))

# similar to above but we append coordinates
#  now return the paths took to reach the destination coordinate
def mazePathCount(destCoordinates):
    def counter(destCoordinates, currPos, pathCoord, res):
        if currPos[0] > destCoordinates[0] or currPos[1] > destCoordinates[1]: 
            return
        if currPos[0] == destCoordinates[0] and currPos[1] == destCoordinates[1]: 
            res.append(pathCoord)
            return 
        
        # recursion logic
        counter(destCoordinates, [currPos[0]+1,currPos[1]], pathCoord+ [[currPos[0]+1,currPos[1]]] , res)
        counter(destCoordinates, [currPos[0],currPos[1]+1], pathCoord+ [[currPos[0],currPos[1]+1]], res)
    
    currPos = [0,0]
    res = []
    pathCoord = []
    counter(destCoordinates, currPos, pathCoord, res)
    return res

ans = mazePathCount([2,2])
for ls in ans:
    print(ls)
    