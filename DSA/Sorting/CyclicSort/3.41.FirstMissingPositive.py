def firstMissingPositive(nums):
    def swap(i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    i = 0
    while i < len(nums):
        correctIndex = nums[i] -1
        if correctIndex >= 0 and correctIndex < len(nums) and nums[i] != nums[correctIndex]: # correct index in the range of (0, len)
            swap(i, nums[i] -1)
        else:
            i+=1
    
    i = 0
    while i < len(nums):
        if nums[i]!= i+1:
            return i+1
        i+=1
        
    return len(nums)+1
nums = [7,8,9,11,12]
print(firstMissingPositive(nums))