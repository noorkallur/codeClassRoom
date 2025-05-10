from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part_list =[]

        def isPali(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            
            return True

        def backtrack(idx):
            if idx >= len(s):
                res.append(part_list[:])
                return

            for i in range(idx, len(s)):
                if isPali(idx, i) == True:
                    part_list.append(s[idx:i+1])
                    backtrack(i+1)
                    part_list.pop()
            
        backtrack(0)
        return res