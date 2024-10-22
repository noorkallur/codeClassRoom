# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# https://youtu.be/zx5Sw9130L0
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i, val in enumerate(heights):
        last_index = i
        while stack and val <= stack[-1][1]:
            last_index = stack[-1][0]
            area = stack[-1][1] * (i - last_index)
            print(area)
            if max_area < area:
                max_area = area
            stack.pop()
                
        stack.append([last_index, val])
    print(stack)        
    while stack:
        area = stack[-1][1] * (len(heights) - stack[-1][0])
        if max_area < area:
            max_area = area 
        stack.pop()
        
    return max_area


heights = [2,1,5,6,2,3]
# heights = [2,4]s
# heights = [1,1]
print(largestRectangleArea(heights))