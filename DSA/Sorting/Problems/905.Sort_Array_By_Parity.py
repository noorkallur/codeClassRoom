# https://leetcode.com/problems/sort-array-by-parity/
def sort_array_by_parity(nums):
    s = 0
    e = len(nums) - 1
    
    while s < e:
        while s < e  and nums[s] %2 == 0: #make sure s does not outofbounds
            s +=1
        while s < e and nums[e] %2 != 0: #make sure e does not outofbounds
            e -=1
    
        if s < e:
            nums[s], nums[e] = nums[e], nums[s] #swap
            s +=1
            e -=1
    return nums
        
nums = [0]
nums = [0,2]
nums = [3,1,2,4,8,9,0,7]
nums = [3,1,2,4,8]
print(sort_array_by_parity(nums))