# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Intuition is that we keep appending to the list, as soon the list is equals to k then return from recursion
# how to exit recursion:
# return true only when list has the k elements otherwise false
class Solution:
    def kthSmallest(self, root:TreeNode, k: int) -> int:
        def kthSmallest_helper(root, k):
            if root == None:
                return False
            
            if kthSmallest_helper(root.left, k):
                return True
            # check if we are found the kth element    
            num_list.append(root.val)
            if len(num_list) == k:
                return True
                
            return kthSmallest_helper(root.right, k)
        
        num_list = []
        kthSmallest_helper(root, k)
        return num_list[k-1]
    

# Different return mechanism
class Solution:
    def kthSmallest(self, root:TreeNode, k: int) -> int:
        def kthSmallest_helper(root, k):
            if root == None:
                return None
            
            left = kthSmallest_helper(root.left, k)
            if left!= None:
                return left

            # check if we are found the kth element    
            num_list.append(root.val)
            if len(num_list) == k:
                return num_list[k-1]
                
            return kthSmallest_helper(root.right, k)

        num_list = []
        return kthSmallest_helper(root, k)
    


         
        