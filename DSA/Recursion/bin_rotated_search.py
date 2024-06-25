def rotated_pivot(arr):
    s = 0
    e = len(arr)-1
    
    if arr[s]<=arr[e]:
        return -1
    
    while s < e:
        mid = (s+e)//2
        if arr[mid] > arr[mid+1]:
            return mid
        if arr[mid] > arr[e]:
            s = mid
        else:
            e = mid - 1
            
    return -1
# print(rotated_pivot([10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(rotated_pivot([ 1, 2, 3, 4, 5, 6, 7, 8]))
# print(rotated_pivot([ 2, 1]))

def recursiveBS(s, e, nums, target):
    while s<=e:
        mid = (s+e)//2
        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            return recursiveBS(s, mid-1, nums, target) 
        else:
            return recursiveBS(mid+1, e, nums, target)
    return -1

def helper_func(arr, target, pivot):
    s = 0
    e = len(arr)-1
    # print(f"pivot{pivot}")
    if pivot == -1:
        return recursiveBS(s, e, arr, target)
    else:
        if target < arr[pivot]:
            return recursiveBS(pivot+1, e, arr, target) 
        else:
            return recursiveBS(s, pivot, arr, target) 
 
def pivotSearch(arr, target):
    return helper_func(arr, target, rotated_pivot(arr))


print(pivotSearch([10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8], 3))
print(pivotSearch([ 1, 2, 3, 4, 5, 6, 7, 8], 3))
print(pivotSearch([ 1, 2, 3, 4, 5, 6, 7, 8], -1))
print(pivotSearch([ 2, 1], 1))
