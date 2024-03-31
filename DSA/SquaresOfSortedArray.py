def sortedSquares(nums):
    first = 0
    last = len(nums) - 1
    newNums = []
    while(first <= last):
        if abs(nums[first]) >= abs(nums[last]):
            newNums.append( nums[first] * nums[first] )
            first +=1
        else:
            newNums.append( nums[last] * nums[last])
            last -= 1
    return newNums[::-1]

print(sortedSquares([-4,-1,0,3,10]))