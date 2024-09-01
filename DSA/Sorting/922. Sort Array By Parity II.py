def findEven(nums, s):
    end = len(nums)-1
    while end < s:
        if nums[end]%2 ==0:
            return end
        e+=1
    return -1

def findOdd(nums, s):
    end = len(nums)-1
    while end < s:
        if nums[end]%2 ==1:
            return end
        e+=1
    return -1

def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def sortArrayByParityII(nums):
    s=0
    while s < len(nums) -1 -1:
        if s%2 == 0:
            if nums[s]%2 != 0:
                ret = findEven(nums, s)
                swap(ret, s, nums)
        else:
            if nums[s]%2 != 1:
                ret = findOdd(nums, s)
                swap(ret, s, nums)  
        s+=1

nums = [7, 3, 4, 2]
sortArrayByParityII(nums)
print(nums)

#another solution using two pointer method
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
def sort_array_by_parity_II(nums):
    length = len(nums)
    even_ptr = 0
    odd_ptr = 1
    while even_ptr < length and odd_ptr < length:
        while even_ptr < length and nums[even_ptr]%2 == 0: #make sure even_ptr does not outofbounds
            even_ptr +=2
        
        while odd_ptr < length and nums[odd_ptr]%2 != 0: #make sure odd_ptr does not outofbounds
            odd_ptr +=2
        
        if even_ptr < length and odd_ptr < length: #make sure even_ptr, odd_ptr does not outofbounds
            nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr] # swap
            even_ptr +=2
            odd_ptr +=2
    
    return nums

nums = [4,2,5,7]
nums = [2,3]
print(sort_array_by_parity_II(nums))