# # https://leetcode.com/problems/find-in-mountain-array/description/
def mountainIndexOfArray(nums):
    s = 0
    e = len(nums)
    while s < e:
        mid = (s + e)//2
        if nums[mid] > nums[mid+1]:
            e = mid
        else:
            s = mid + 1
    return e


def binsearchIndexBase(arr, target, start, end, ascneding = True):
    if ascneding == True:
        while(start <= end):
            mid = (start + end)//2
            if arr[mid] > target:
                end = mid -1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
    else:
        while(start <= end):
            mid = (start + end)//2
            if arr[mid] < target:
                end = mid -1
            elif arr[mid] > target:
                start = mid + 1
            else:
                return mid
        return -1
        

def findInMountainArray(arr, target):
    mountIndex = mountainIndexOfArray(arr)
    print(mountIndex)
    ansIndex = binsearchIndexBase(arr, target, 0, mountIndex) 
    print(ansIndex)
    if ansIndex == -1:
        ansIndex = binsearchIndexBase(arr, target, mountIndex + 1, len(arr) -1, False)
    print(ansIndex)
    return ansIndex  


arr = [1,2,3,4,5,3,1]
# print(findInMountainArray(arr, 3))
arr = [0,1,2,4,2,1]
# print(findInMountainArray(arr, 3))
arr = [0,5,3,1]
print(findInMountainArray(arr, 1))