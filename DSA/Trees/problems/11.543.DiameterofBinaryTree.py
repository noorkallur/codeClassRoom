class Solution:
    def __init__(self):
        self.max_diam = 0

    def diameterOfBinaryTree(self, root) -> int:
        self.height(root)
        return self.max_diam 

    def height(self, root):
        if root == None:
            return - 1
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        self.max_diam = max(self.max_diam, (left_height + right_height + 2)) # a place to store the max diam

        return max(left_height, right_height)+1