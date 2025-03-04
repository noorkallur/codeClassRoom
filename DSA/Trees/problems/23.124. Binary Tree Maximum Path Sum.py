# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        def maxPathSum_helper(root):
            nonlocal max_path_sum
            if root == None:
                return 0
            # if root.left == None and root.right == None:
            #     return root.val

            left_sum = maxPathSum_helper(root.left)
            right_sum = maxPathSum_helper(root.right)

            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)
            max_path_sum = max(root.val + left_sum + right_sum, max_path_sum)
            return max(left_sum, right_sum) + root.val

        max_path_sum = float('-inf')
        maxPathSum_helper(root)
        return max_path_sum



        