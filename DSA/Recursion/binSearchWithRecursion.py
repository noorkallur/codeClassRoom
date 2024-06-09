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
nums = [2, 6, 7, 9, 11]
print(recursiveBS(0, len(nums)-1, nums, 12))