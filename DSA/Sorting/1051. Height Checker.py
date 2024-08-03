# https://leetcode.com/problems/height-checker/
def heightChecker(heights):
    expected = heights.copy()
    expected.sort()
    i = 0
    ans = 0
    while i < len(heights):
        if expected[i] != heights[i]:
            ans +=1
        i+=1
    return ans


heights = [1,1,4,2,1,3]
print(heightChecker(heights))