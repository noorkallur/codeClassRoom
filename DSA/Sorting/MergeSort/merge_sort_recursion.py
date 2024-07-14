def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    left = merge_sort(nums[0:mid]) # left most array
    right = merge_sort(nums[mid:len(nums)]) # right most array
    
    return merge(left, right)# merge and sort the divided array
    

def merge(left, right):
    i = 0
    j = 0
    merged_array = [] #merged left and right goes here
    while i < len(left) and j <len(right): #  two pointer method to find the smallest from each array, append it to the merged array
        if left[i] < right[j]:
            merged_array.append(left[i])
            i +=1
        else:
            merged_array.append(right[j])
            j +=1
            
    # add remaining elements of the remaining array
    while i < len(left):
        merged_array.append(left[i])
        i +=1
    
    while j < len(right):
        merged_array.append(right[j])
        j +=1
        
    return merged_array

nums = [4, 3, 2, 1, 78, 56, 34, 235, 809, 2, 5, 234, 57]
# nums = []
print(merge_sort(nums))
