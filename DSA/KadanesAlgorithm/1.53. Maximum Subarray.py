# https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray(nums):
    subArrSum = nums[0]
    maxSubSum = subArrSum

    for i in range(1, len(nums)):
        curr = nums[i]
        if subArrSum + curr> curr:
            subArrSum +=curr
        max(subArrSum, subArrSum)
    
    return maxSubSum



nums = [-2,1,-3,4,-1,2,1,-5,4]
