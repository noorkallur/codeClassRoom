def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
    
def insertionSort(nums): 
    end = len(nums) - 1 #end Index
    for i in range(0, end):# for 5 element array, starts at 0 ends at 4 i.e at val 4 doesnot enter loop, hence i = 0, 1, 2, 3
        j = i + 1 #this is the reason why we only check till end - 1
        while j > 0:
            if nums[j-1] > nums[j]:
                swap(j, j-1, nums)
            else:
                break
            j -= 1 
        
        
arr = [5, 4, 3, 2, 1]
insertionSort(arr)
print(arr)