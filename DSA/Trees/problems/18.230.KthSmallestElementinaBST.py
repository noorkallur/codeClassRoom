# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root:TreeNode, k: int) -> int:
        def kthSmallest_helper(root, k):
            if root == None:
                return False
            
            if kthSmallest_helper(root.left, k):
                num_list.append(root.val)
                if len(num_list) == k:
                    return True
                
            return kthSmallest_helper(root.left, k)
        
        num_list = []
        kthSmallest_helper(root, k)
        return num_list[k-1]