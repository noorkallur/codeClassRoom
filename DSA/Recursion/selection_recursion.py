def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
    
def selection_recursion(nums, highest, i, j):
    if i >= len(nums):
        return
    if j < len(nums) - i:
        if nums[highest] < nums[j]:
            highest = j
        return selection_recursion(nums, highest, i, j+1)
    else:
        swap(highest, len(nums)-1-i, nums)
        return selection_recursion(nums, 0, i+1, 1)


nums = [5, 4, 3, 2, 1]
selection_recursion(nums, 0, 0, 1)
print(nums)