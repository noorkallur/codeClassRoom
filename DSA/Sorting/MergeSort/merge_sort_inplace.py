# MERGE SORT in place using recursion : Merge sort using ONLY original array, we need the track of index

# 1. Before writing recursion function, first think of how "merge" funciton should be
#       a. it needs start, mid and end 
#               => range of left = start till mid(inclusive)
#               => range of right = mid+1 till end(inclusive){why inclusive: we are passing ablsoulte index}
#       b. left loop runs till mid(inclusive) and right loop runs till end(inclusive). append the lowest element to local array{why local, its not possible to swap them in place of original array as it would jumble the comparisons}
#       c. add the remaining elements if left/right contains any
#       d. update the original array using local array
# 2. Recursive function should split the array into two parts
#       a. divide by 2 till you only have ONE element.
#       b. left half will be sorted first and then right half
#       c. first merge function with TWO, FOUR, EIGHT ,...etc

def merge_sort(nums, startIndx, endIndx):
    if startIndx >= endIndx:
        return 
    
    mid = (endIndx + startIndx)//2
    merge_sort(nums, startIndx, mid)
    merge_sort(nums, mid+1, endIndx)
    
    merge(nums, startIndx, mid, endIndx)


def merge(nums, start, mid, end):
    leftp = start
    rightp = mid + 1
    merge_array = []
    
    while leftp <= mid and rightp <= end:
        if nums[leftp] < nums[rightp]:
            merge_array.append(nums[leftp])
            leftp+=1
        else:
            merge_array.append(nums[rightp])
            rightp+=1
            
    while leftp <= mid:
        merge_array.append(nums[leftp])
        leftp+=1
    
    while rightp <= end:
        merge_array.append(nums[rightp])
        rightp+=1
    
    for i in range(0, len(merge_array)):
        nums[start + i] = merge_array[i]
 
nums = [4, 3, 2, 1, 78, 56, 34, 235, 809, 2, 5, 234, 57]
# nums = [4, 3, 2, 1]
# nums = []
merge_sort(nums, 0, (len(nums)-1))
print(nums)
