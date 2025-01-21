# quesion at this point of video: just onnly look at question and try to answer(if needed look at thinking process below) https://youtu.be/zg5v2rlV1tM?si=NsIzabWFW_hYfO1l&t=192
# Rules: 
# 1.person starts at 0,0 
# 2.can only moce Right direction  or Down direction one step at a time
# thinking process :
# 1. think of this as coordinates
# 2. goal is to get to the (2,2)
# 3. reduce col, row recursively
# 4. Notice as soon as you reach 2 in col or row there is one direction you can reach to 2,2(because of the rules) draw it out

def mazePathCount(destCoordinates):
    def counter(destCoordinates, currPos):
        if currPos[0] > destCoordinates[0] or currPos[1] > destCoordinates[1]: # if the currPos goes pas the dest coordinate then return 0
            return 0
        if currPos[0] == destCoordinates[0] or currPos[1] == destCoordinates[1]: # if the currPos reaches the dest coordinate then return 1
            return 1
        
        # recursion logic
        return counter(destCoordinates, [currPos[0]+1,currPos[1]]) +  counter(destCoordinates, [currPos[0],currPos[1]+1])
    
    currPos = [0,0]
    return counter(destCoordinates, currPos)

print(mazePathCount([2,2]))

            
    