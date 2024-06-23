def linear_search(nums, target):
    i = 0
    return helper_fun(nums, target, i)

def helper_fun(nums, target, i):
    if i == len(nums):
        return -1
    if nums[i] == target:
        return i
    else:
        return helper_fun(nums, target, i+1)
    
print(linear_search([1, 3, 5, 67, 89], 67))
print(linear_search([1, 3, 685, 67, 89], 89))
print(linear_search([1, 3, 685, 67, 89], 8))
print(linear_search([1, 3, 685, 67, 89], 1))
