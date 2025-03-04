# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def sumNumbers_helper(root, r_to_l):
            if root == None:
                return
            if root.left == None and root.right == None:
                all_paths.append(r_to_l+str(root.val))
                return 
            
            sumNumbers_helper(root.left, r_to_l+str(root.val))
            sumNumbers_helper(root.right, r_to_l+str(root.val))


        r_to_l = ""
        all_paths = []
        sumNumbers_helper(root, r_to_l)

        #sum the array of num strings
        sum = 0
        for snum in all_paths:
            sum +=int(snum)

        return sum
        
        