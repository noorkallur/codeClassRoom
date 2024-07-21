# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# https://youtu.be/W9QJ8HaRvJQ?t=10120&si=9s4X981GW_5nXNMw
def findPivot(arr):
    """_summary_
    Return pivot if present or else return the end of the array i.e greatest value
    technically returns the greatest value in a rotated array
    """
    s = 0
    e = len(arr) - 1
    while s < e:
        mid = (s+e)//2
        if arr[mid] > arr[mid + 1]: # return logic
            return mid
        elif arr[s] > arr[mid]: #trim the right part
            e = mid - 1
        else: # trim the left part
            s = mid + 1
    return e #if only one or two elements are present return the e 

def findPivotAlt(nums):
    s = 0
    e = len(nums) -1
    while(s<=e):
        mid = (s+e)//2
        if mid != e and nums[mid] > nums[mid + 1]:
            return mid
        if mid != s and nums[mid] <  nums[mid - 1]:
            return mid - 1
        if nums[mid] > nums[e]:
            s = mid + 1
        else:
            e = mid - 1
    return - 1

def binsearchIndexBase(arr, target, start, end):
    while(start <= end):
        mid = (start + end)//2
        if arr[mid] > target:
            end = mid -1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1
    
    
def SearchInRotatedArrayBS(arr, target):
    pivotIndex = findPivot(arr)
    ans = -1
    if target >= arr[0] : # target >= start means target must be right side of pivot(all lesser vallues)
        ans = binsearchIndexBase(arr, target, 0, pivotIndex )
    else: # target < start means target must be left side of pivot(all large values)
        ans = binsearchIndexBase(arr, target, pivotIndex + 1, len(arr) - 1)
    return ans
    
# print(SearchInRotatedArrayBS([10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8], 6)) #9
# print(SearchInRotatedArrayBS([1, 2, 3, 4, 5, 6, 7, 8], 3)) #2
# print(SearchInRotatedArrayBS([1, 2], 2))#1
# print(SearchInRotatedArrayBS([2, 1], 2))#0
# print(SearchInRotatedArrayBS([2, 1], 1))#1

print(findPivot([2,9,2,2,2]))




    
