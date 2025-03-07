from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        if not root:
            return output
        q = deque()
        q.append(root)
        while len(q):
            q_size=len(q)
            max_val = float('-inf')
            for _ in range(q_size):
                node = q.popleft()
                max_val=max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            output.append(max_val)
        
        return output