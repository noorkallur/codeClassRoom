# https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=sliding-window
def findLHS(nums):
    max_sub_len = 0
    winStart, winEnd = 0, 0
    nums.sort()
    for winEnd in range(len(nums)):
        while winStart < winEnd and nums[winEnd] - nums[winStart] > 1:
            winStart += 1
        if nums[winEnd] - nums[winStart] == 1:
            max_sub_len = max(winEnd-winStart+1, max_sub_len)
    return max_sub_len

nums = [1,3,2,2,5,2,3,7] #5
nums = [1,2,3,4] #2
nums = [1,1,1,1] #0
nums = [1] #0
nums = [1, 2] #2
print(findLHS(nums))