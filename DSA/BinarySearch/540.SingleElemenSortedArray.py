# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
def binarySearchIndexBased(array, target, indxStart, indxEnd):
    start = indxStart
    end = indxEnd
    while start <= end:
        mid = int((start + end)/2) 
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1
def singleNonDuplicate(nums):
    s = 0
    e = len(nums) - 1
    while(s <= e):
        mid = (s + e)//2
        if -1 != binarySearchIndexBased(nums, nums[mid], s, mid - 1):
            if 0 != (mid - s + 1)%2: 
                e = mid - 2
            else:
                s = mid + 1
        elif -1 != binarySearchIndexBased(nums, nums[mid], mid + 1, e):
            if 0 != (e - mid + 1)%2: 
                s = mid + 2
            else:
                e = mid - 1
        else:
            return mid
    return -1

arr = [1,1, 2, 3,3]
arr = [1,1, 2,2, 3,3, 4, 5,5]
arr = [1, 2,2, 3,3, 4,4, 5,5]
arr = [3,3,7,7,10,11,11]
arr = [1,1, 3, 5,5, 6,6, 7,7]
print(singleNonDuplicate(arr))