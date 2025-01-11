# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
def maxScore(cardPoints, k):
    total = sum(cardPoints)
    left = 0
    curr_sum = sum(cardPoints[0:len(cardPoints)-k])
    ans = total - curr_sum
    for right in range(len(cardPoints)-k, len(cardPoints)):
        curr_sum = curr_sum + cardPoints[right] - cardPoints[left]
        left +=1
        if (total - curr_sum) > ans:
            ans = total - curr_sum 
    return ans

def maxScoreNoorAlt(nums, k):
    total_sum = sum(nums)
    winSize = len(nums) - k
    currSum = sum(nums[:winSize])
    maxSubSum = total_sum - currSum
    for winEnd in range(winSize, len(nums)):
        currSum = currSum + nums[winEnd] - nums[winEnd-winSize]
        maxSubSum = max(maxSubSum, total_sum - currSum)
    return maxSubSum

cardPoints = [1,2,3,4,5,6,1]
k = 3
cardPoints = [2,2,2]
k = 2
cardPoints = [9,7,7,9,7,7,9]
k = 7
cardPoints = [9,7]
k = 2
cardPoints = [9]
k = 1
cardPoints = [9]
k = 0
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
print(maxScore(cardPoints, k))