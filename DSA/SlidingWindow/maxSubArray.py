def maxSubArray(nums, k):
    maxsum = 0
    curr_sum = 0
    for i in range(0, len(nums)):
        if i < k:
            curr_sum = curr_sum + nums[i]
            continue
        curr_sum = curr_sum - nums[i-k] + nums[i]
        if curr_sum > maxsum:
            maxsum = curr_sum
    return maxsum

nums = [1, 4, 7, 2, 4, 8, 3, 2, 5]
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(maxSubArray(nums, 3))
        
           