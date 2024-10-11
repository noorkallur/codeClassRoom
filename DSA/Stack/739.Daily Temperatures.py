# https://leetcode.com/problems/daily-temperatures/
from typing import List

class NoorSolution: # o(n) too slow
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  
        ans = []
        curr_stk = []
        for i in range(0, len(temperatures)):
            if curr_stk:
                ans.append(0)
                curr_stk.clear()
            curr_stk.append(temperatures[i])
            for j in range( i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(len(curr_stk))
                    curr_stk.clear()
                    break
                else:
                    curr_stk.append(temperatures[j])
        if curr_stk:
            ans.append(0)
        return ans
    
object = NoorSolution()
temperatures = [73,74,75,71,69,72,76,77]
temperatures = [30,40,50,60]
temperatures = [30]
temperatures = []
temperatures = [55,38,53,81,61,93,97,32,43,78]

print(object.dailyTemperatures(temperatures))

# Monotonic stack https://www.geeksforgeeks.org/introduction-to-monotonic-stack-2/
# This soultion is more like a Monotonic decreasing stack as we pop the element if its greater. if its lower we keep appending to stack
# leet soln:  https://youtu.be/cTBiBSnjO3c

class Solution: # 0(n) much better and faster
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  
        ans = [0] * len(temperatures)
        index_stack = []
        for i in range(0, len(temperatures)):
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]: # check new temp added is warmer to all our temp already added to index_stack  
                ans_idx = index_stack.pop()
                ans[ans_idx] = i - ans_idx  # wait days is simply subtracting the warmer index - the lower temp
            
            index_stack.append(i) # only add new index after our comparisions of temps
        return ans
            

    
object = Solution()
temperatures = [73,74,75,71,69,72,76,77]
# temperatures = [30,40,50,60]
# temperatures = [30]
# temperatures = []
# temperatures = [55,38,53,81,61,93,97,32,43,78]

print(object.dailyTemperatures(temperatures))