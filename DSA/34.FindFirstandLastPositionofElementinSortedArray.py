def floorOfTargetInArray(nums, target):
    s = 0 
    e = len(nums) -1
    if nums[s] > target:
        return -1
    while s <= e:
        mid = int((s+e)/2)
        if nums[mid] == target:
            if nums[mid-1] < target:
                return mid
            else:
                e = mid - 1 
        if nums[mid] < target:
            s = mid + 1
        elif nums[mid] > target:
            e = mid -1  
    return -1
def ceilOfTargetInArray(nums, target):
    s = 0 
    e = len(nums) -1
    if nums[e] < target:
        return -1
    while s <= e:
        mid = int((s+e)/2)
        if nums[mid] == target:
            if nums[mid+1] > target:
                return mid
            else:
                s = mid + 1
        if nums[mid] < target:
            s = mid + 1
        elif nums[mid] > target:
            e = mid -1  
    return -1     
def searchRange(nums, target):
    length = len(nums) 
    if length == 0:
        return -1,-1
    s = 0 
    e = length - 1
    if nums[s] == target:
        lowIndex = s
    else:
        lowIndex = floorOfTargetInArray(nums, target) 
    if nums[e] == target:
        greatIndex = e
    else:
        greatIndex = ceilOfTargetInArray(nums, target)
    return(lowIndex, greatIndex )

# print(searchRange([5,7,7,8,8,10], 8)) #3, 4
# print(searchRange([8,8,8,8,8,8], 8))#0,5
# print(searchRange([8,8,8,8,8,9], 8))#0,4
# print(searchRange([8,8,8,8,8,9], 9))#5,5
# print(searchRange([8,8,8,8,8,9], 10))#-1, -1
# print(searchRange([], 0))#-1 ,-1

## better code from dev
def binarySearchTwoWay(nums, target, searchLeft=False): # same solution but optimized to not to do unnecessary checks
    s = 0 
    e = len(nums) -1
    ans = -1
    while s <= e:
        mid = int((s+e)/2)
        if nums[mid] < target:
            s = mid + 1
        elif nums[mid] > target:
            e = mid -1 
        else:
            ans = mid
            if searchLeft:
                e = mid - 1
            else:
                s = mid + 1
    return ans     
def searchRange(nums, target):
    ans = [-1, -1]
    ans[0] = binarySearchTwoWay(nums, target, True) 
    if ans[0]!= -1:
        ans[1] = binarySearchTwoWay(nums, target)
    return ans

print(searchRange([5,7,7,8,8,10], 8)) #3, 4
print(searchRange([8,8,8,8,8,8], 8))#0,5
print(searchRange([8,8,8,8,8,9], 8))#0,4
print(searchRange([8,8,8,8,8,9], 9))#5,5
print(searchRange([8,8,8,8,8,9], 10))#-1 , -1
print(searchRange([], 0))#-1 ,-1
