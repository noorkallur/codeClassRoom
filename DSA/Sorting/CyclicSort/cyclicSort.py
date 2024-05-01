#only works for 1 to N range
def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
    
def cyclicSortNoor(nums):  
    i = 0    
    end = len(nums) -1
    while i < end:
        if i != nums[i] -1:
            swap(i, nums[i] -1, nums)
        else:
            i +=1

def cyclicSort(nums):  
    i = 0    
    end = len(nums) -1
    while i < end:
        correctIndex = nums[i] -1
        if nums[i] != nums[correctIndex]:
            swap(i, nums[i] -1, nums)
        else:
            i +=1
            
arr = [5, 4, 3, 2, 1]
cyclicSort(arr)
print(arr)