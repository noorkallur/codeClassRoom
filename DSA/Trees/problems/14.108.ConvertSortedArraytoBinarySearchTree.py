# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_helper(self.root, value)

    def insert_helper(self, root, value):
        if root == None:
            return TreeNode(value)

        if root.val > value:
            root.left = self.insert_helper(root.left, value)
        else:
            root.right = self.insert_helper(root.right, value)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBST_helper(start, end):
            if start > end:
                return

            mid = (start + end)//2

            self.insert(nums[mid])

            sortedArrayToBST_helper(start, mid-1)
            sortedArrayToBST_helper(mid+1, end)

        s = 0
        e = len(nums) -1
        sortedArrayToBST_helper(s, e)
        return self.root
