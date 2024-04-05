# https://leetcode.com/problems/minimum-common-value/description/
def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid =int((start + end)/2)
        if nums[mid]==target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        if nums[mid] > target:
            end = mid - 1
    return -1

def getCommon(array1, array2):
    for num in array1:
        if(binarySearch(array2, num) != -1):
            return num
    return -1

array1 = [1,2,3]
array2 = [2,4]
print(getCommon(array1, array2))
array1 = [1,2,3]
array2 = [5,4]
print(getCommon(array1, array2))