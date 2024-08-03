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