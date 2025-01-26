# AKA sinking sort OR exchange sort
# number of iterations needed n-1 times (as the last one element will be smallest)
def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def bubbleSort(nums):  
    for i in range(0, len(nums) - 1):
        for j in range(1,  len(nums) - i):
            if nums[j] < nums[j-1]:
                swap(j , j-1, nums)


arr = [5, 4, 3, 2, 1]
bubbleSort(arr)
print(arr)

def UpdatedbubbleSort(nums):
    for i in range(0, len(nums) - 1):
        swapped = False
        for j in range(1,  len(nums) - i):
            if nums[j] < nums[j-1]:
                swap(j , j-1, nums)
                swapped = True
        if not swapped:
            break
        
        
arr = [5, 4, 3, 2, 1]
UpdatedbubbleSort(arr)
print(arr)