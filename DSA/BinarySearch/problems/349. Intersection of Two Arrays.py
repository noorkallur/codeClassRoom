# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        # mid = int(start + (end - start)/2) # no need
        mid = int((start + end)/2) # python3 has no max int limit hence mid = (start + end)/2 works
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1

def intersection(nums1, nums2):
    if nums1 < nums2:
        return intersection(nums2, nums1)
    nums1.sort()
    nums2.sort()
    output =[]
    for num in nums2:
        ret = binarySearch(nums1,num)
        if ret != -1:
            output.append(nums1[ret])
            nums1.pop(ret)
            
    return output

nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1 = [1,2,2,1]
nums2 = [1,1]
print(intersection(nums1, nums2))