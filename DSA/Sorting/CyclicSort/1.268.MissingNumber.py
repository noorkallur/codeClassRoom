# https://leetcode.com/problems/missing-number/description/
def missingNumber(nums):
    def swap(i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    i=0
    while i < len(nums):
        if 0 != nums[i] and i != nums[i]-1:
            swap(i, nums[i]-1)
        else:
            i += 1
    
    for i in range(0, len(nums)):
        if 0 == nums[i]:
            return i+1
    return 0

arr = [0, 4, 3, 2, 1]
print(missingNumber(arr))
arr = [3,0,1]
print(missingNumber(arr))
arr = [1]
print(missingNumber(arr))
    