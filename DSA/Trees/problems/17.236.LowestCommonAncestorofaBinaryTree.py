# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# intution
# Find the node first once its found, keep appending along nodes on its path, this is L->R->N,
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = []
        q_list = []

        def populate_list(root, target, dfs_list):
            if root == None:
                return False

            if root == target:
                dfs_list.append(root)
                return True

            left_res = populate_list(root.left, target, dfs_list)
            right_res = populate_list(root.right, target, dfs_list)
                
            if left_res or right_res:
                dfs_list.append(root)
                return True
            else:
                return False
        
        populate_list(root, p, p_list) #list is from p to root
        populate_list(root, q, q_list) #list is from q to root
        
        # the first that matches from the both the list
        for p in p_list:
            if p in q_list:
                return p


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left and not right:
            return None

        if left and not right:
            return left
        elif right and not left:
            return right
        else:
            return root
            
        
               