def findPeak(nums):
    s = 0
    e = len(nums) - 1
    while s <  e :
        mid = (s+e)//2
        if nums[mid] <=  nums[mid+1]:
            s = mid + 1
        else:
            e = mid
    return e
    
# print(findPeak([1, 2, 2, 3, 4, 5, 1]))
# print(findPeak([5, 4, 3, 2]))
# print(findPeak([5, 2, 2, 3, 4, 5, 6, 7, 5, 4, 3, 3, 1]))

def findPeak(nums):
    s = 0
    e = len(nums) - 1
    while s <  e :
        mid = (s+e)//2
        if (mid != e or mid != s) and (nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
            return mid
        if nums[mid] <=  nums[mid+1]:
            s = mid + 1
        else:
            e = mid
    return e
print(findPeak([1,2,3,2,1]))
print(findPeak([1, 2, 2, 3, 4, 5, 1]))
print(findPeak([5, 4, 3, 2]))
print(findPeak([5, 2, 2, 3, 4, 5, 6, 7, 5, 4, 3, 3, 1]))