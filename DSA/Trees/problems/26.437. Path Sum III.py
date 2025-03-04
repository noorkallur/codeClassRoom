# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def path_counter():
            count = 0
            curr_sum =0
            for i in range(len(num_list)-1, -1, -1):
                curr_sum+= num_list[i]
                if curr_sum == targetSum: # if target sum is found increment
                    count +=1
            return count

        def pathSum_helper(root):
            if root == None:
                return 0
                
            num_list.append(root.val)

            count = pathSum_helper(root.left)
            count += pathSum_helper(root.right)

            # check how many paths can be made
            count +=path_counter()

            #backtrack and pop 
            num_list.pop()

            return count

        num_list =[]
        return pathSum_helper(root)


        
