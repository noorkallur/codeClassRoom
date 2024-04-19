# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# Noor solution
def peakIndexInMountainArray(arr: list[int]) -> int:
    s= 0
    e= len(arr) - 1
    while s <= e:
        mid = int((s + e)/2)
        if arr[mid]>arr[mid+1]:
            if mid != 0 and arr[mid]>arr[mid-1]: # need to check if the mid == 0 that means only two elements are present and loop will not break[s, e]
                return mid
            else:
                e = mid - 1
        else:
            s= mid + 1
    return - 1

print(peakIndexInMountainArray([3,9,8,6,4]))
print(peakIndexInMountainArray([3,4,5,1]))
print(peakIndexInMountainArray([0,10,5,2]))    
print(peakIndexInMountainArray([1, 2, 3, 4, 10, 12, 2, 1, 0]))
print(peakIndexInMountainArray([1, 2, 2, 2, 11, 12, 2, 1, 0]))


# dev solution
# the goal with this function is to reduce the s and e to one element ie point to the same element(break if s==e) by eliminating the lesser value elements
def peakIndexInMountainArray(arr: list[int]) -> int:
    s= 0
    e= len(arr) - 1
    while s < e:
        mid = int((s + e)/2)
        if arr[mid]>arr[mid+1]:
            e = mid
        else:
            s = mid + 1
    return e # return s does not matter as both are same

print(peakIndexInMountainArray([3,9,8,6,4]))
print(peakIndexInMountainArray([3,4,5,1]))
print(peakIndexInMountainArray([0,10,5,2]))    
print(peakIndexInMountainArray([1, 2, 3, 4, 10, 12, 2, 1, 0]))
print(peakIndexInMountainArray([1, 2, 2, 2, 11, 12, 2, 1, 0]))