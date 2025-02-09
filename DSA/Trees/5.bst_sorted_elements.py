class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

class BST:
    def __init__(self):
        self.root = None
        
    def prettyDisplay(self):
        self.prettyDisplay_helper(self.root, 0)
    
    def prettyDisplay_helper(self, parentNode, level):
        if parentNode == None:
            return # as soon as we dont have anything print that many tabs and pring number at the end
        
        # find the last right node
        self.prettyDisplay_helper(parentNode.right, level+1)
        
        if level != 0:
            for i in range(level-1):
                print("|\t", end="")
            print(f"|------>{parentNode.val}({parentNode.height})")
        else:
            print(f"{parentNode.val}({parentNode.height})")
         
        # left in that level 
        self.prettyDisplay_helper(parentNode.left, level+1)  
    
    def height(self, node):
        if node == None:
            return -1 # empty node height is -1
        return node.height
    
    def insert_value(self, val):
        self.root = self.insert_value_helper(self.root, val) 
        return
    
    def insert_value_helper(self, parentNode, val):
        if parentNode == None:
            new_node = Node(val) # new node height is 0
            return new_node
        
        if val <= parentNode.val:
            parentNode.left = self.insert_value_helper(parentNode.left, val)
        else:
            parentNode.right = self.insert_value_helper(parentNode.right, val)

        # height of the node, re-assigning height by adding one to the height.this one needs some thinking write it on a paper    
        # 1. we only add 1 extra to the ones we are touching while placing the new node
        # 2. New node height is 0 by default
        parentNode.height = max(self.height(parentNode.left), self.height(parentNode.right)) + 1
        
        return parentNode
    
    def is_balanced(self):
        # traverse through the entire tree to find if there are any nodes which have left and right heights greater than 1
        return self.is_balanced_tree_helper(self.root)
    
    def is_balanced_tree_helper(self, parent_node):
        if parent_node == None:
            return
        
        if abs(self.height(parent_node.left) - self.height(parent_node.right))<=1:
            self.is_balanced_tree_helper(parent_node.left)
            self.is_balanced_tree_helper(parent_node.right)
        else:
            return False
        
        return True  
  
    def insert_sorted_arr(self, nums):
        s = 0
        e = len(nums)-1
        self.insert_sorted_arr_helper(s, e, nums)
        
    def insert_sorted_arr_helper(self, s, e, nums):
        if s > e:
            return
        
        mid = (s+e)//2
        self.insert_value(nums[mid])
        self.insert_sorted_arr_helper(s, mid-1, nums)
        self.insert_sorted_arr_helper(mid+1, e, nums)
        
bst = BST()
nums = [1, 2, 3, 4, 5, 6]
bst.insert_sorted_arr(nums)
bst.prettyDisplay()
print(bst.is_balanced())


bst1 = BST()
nums = [35, 43, 86, 99, 123, 564]
bst1.insert_sorted_arr(nums)
bst1.prettyDisplay()
print(bst1.is_balanced())

