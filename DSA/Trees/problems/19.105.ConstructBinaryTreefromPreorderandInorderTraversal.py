# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def buildTree_helper(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return
        
            root = TreeNode(preorder[0])
            
            index = 0
            for i in range(len(inorder)):
                if preorder[0] == inorder[i]:
                    index = i
                    break
            
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
            root.right= self.buildTree(preorder[i+1:], inorder[i+1:])

            return root

        inorder_index_map = {}
        for i in range(len(inorder)+1):
            inorder_index_map[inorder[i]] = i
        
        return buildTree_helper(preorder, inorder)
    
# some other solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTree_helper(preorder, inorder):
            print(f"pre: {preorder}")
            print(f" imor: {inorder}")
            if len(preorder) == 0 and len(inorder) == 0:
                print("returned")
                return None

            root_val = preorder[0]            
            in_idx = inorder_index_map[root_val]
            i = in_idx - (pre_order_len - len(preorder))
            print(f"index:{i}")
            root = TreeNode(root_val)
            
            root.left = buildTree_helper(preorder[1:i+1], inorder[:i])
            root.right= buildTree_helper(preorder[i+1:], inorder[i+1:])

            return root

        inorder_index_map = {}
        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i
        pre_order_len = len(preorder)
        return buildTree_helper(preorder, inorder)