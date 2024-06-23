def isArraySorted(nums):
    i = 0
    return helper_fun(nums, i)

def helper_fun(nums, i):
    if i == len(nums) - 1:
        return True
    if nums[i] < nums[i+1]:
        return helper_fun(nums, i+1)
    else:
        return False
    
print(isArraySorted([1, 3, 5, 67, 89]))
print(isArraySorted([1, 3, 685, 67, 89]))

def another_helper_fun(nums, i):
    if i == len(nums) - 1:
        return True

    return nums[i] < nums[i+1] and another_helper_fun(nums, i+1)
