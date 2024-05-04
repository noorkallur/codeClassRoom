# https://leetcode.com/problems/find-the-duplicate-number/description/
def findDuplicate(nums):
    def swap(i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
    i = 0
    while i < len(nums):
        correctIndex = nums[i] -1
        if nums[i] != nums[correctIndex]:
            swap(i, nums[i] -1)
        else:
            i+=1
    
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            return nums[i]
        i+= 1
    return -1

nums = [1,3,4,2,2]
nums = [3,3,3,3,3]
nums = [3,1,3,4,2]
print(findDuplicate(nums))
