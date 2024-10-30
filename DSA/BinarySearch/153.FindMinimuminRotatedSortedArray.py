def findMin(nums):
    s = 0
    e = len(nums) -1
    if nums[s] <= nums[e]:
        return nums[s]
    while s <= e:
        mid = (s+e)//2
        
        if mid > 0 and nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[mid] < nums[e]:
            e = mid
        else:
            s = mid +1
    

nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [4,5,1,2,3]
nums = [11,13,15,17]
nums = [1, 2]
nums = [2, 1]
nums = [1, 1]
nums = [1]
print(findMin(nums))