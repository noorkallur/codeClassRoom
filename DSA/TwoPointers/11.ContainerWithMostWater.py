def maxArea(nums):
    left = 0
    right = len(nums) - 1
    max = 0
    while left < right:         
        if nums[left] < nums[right]:
            currArea = nums[left] * (right - left)
            left += 1
        else:
            currArea = nums[right] * (right - left)
            right -= 1
        if currArea > max:
            max = currArea       
        
    return max

    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))