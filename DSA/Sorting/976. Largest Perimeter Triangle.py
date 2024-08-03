def largestPerimeter(nums):
    nums.sort()
    largeperi = 0
    s = 0
    while s < len(nums)-2:
        if nums[s] + nums[s+1] >nums[s+2]:
            if abs(nums[s] - nums[s+1]) < nums[s+2]:
                largeperi = nums[s] + nums[s+1] + nums[s+2]
        s+=1
    return largeperi
    
nums = [2,1,2]
nums = [1,2,1,10]
nums = [3,2,3,4]
print(largestPerimeter(nums))