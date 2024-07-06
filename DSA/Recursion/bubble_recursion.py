def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def bubble_recursion(nums, i, j):
    if i >= len(nums) - 1:
        return
    if j < len(nums) - i:
        if nums[j -1] > nums[j]:
            swap(j, j-1, nums)
            return bubble_recursion(nums, i, j+1)
    else:
         return bubble_recursion(nums, i+1, 1)

        
nums = [5, 4, 3, 2, 1]
bubble_recursion(nums, 0, 1)
print(nums)