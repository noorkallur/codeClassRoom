# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def hasPathSum_helper(root, currSum):
            
            if root == None:
                return False

            currSum +=root.val 
            if currSum == targetSum and root.left == None and root.right == None:
                return True
            
            return hasPathSum_helper(root.left, currSum) or hasPathSum_helper(root.right, currSum)

        return hasPathSum_helper(root, 0)
    