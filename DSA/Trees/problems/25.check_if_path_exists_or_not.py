# Not a leet code question
# you are given a tree with array of path[3,9,12,8]
# return TRUE if the path exists, else return FALSE
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathExists(root:TreeNode, arr) -> bool:
        def pathExists_helper(root:TreeNode, index) -> bool:
            if root == None:
                return False
            
            if root.val !=  arr[index]:
                return False
            
            if root.left == None and root.right == None:
                return True
            
            if pathExists_helper(root.left, index+1):
                return True
            return pathExists_helper(root.right, index+1)
        
            # return pathExists_helper(root.left, index+1) or pathExists_helper(root.right, index+1)
        
        pathExists_helper(root, 0)
