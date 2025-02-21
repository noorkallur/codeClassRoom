
# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root)-> bool:
        def isValidBST_helper(root):
            if root == None:
                return

            isValidBST_helper(root.left)
            num_list.append(root.val)
            isValidBST_helper(root.right)

        num_list = []
        isValidBST_helper(root) # fill the list, now this should be sorted
        
        # check if list is in ascending order or not
        for i in range(len(num_list)-1):
            if num_list[i] >= num_list[i+1]:
                return False
        return True