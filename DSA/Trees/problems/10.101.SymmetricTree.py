from collections import deque 

class Node:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        root_node = int(input("Insert ROOT node: "))
        self.root = Node(root_node)
        self.nodePlacer(self.root)
        
    def nodePlacer(self, parentNode):
        left = input(f"Do you want to place left of {parentNode.val} (y/n): ")
        if left == "y":
            left_value = int(input("Enter left value: "))
            parentNode.left = Node(left_value)
            self.nodePlacer(parentNode.left)
            
        right = input(f"Do you want to place right of {parentNode.val} (y/n): ")
        if right == "y":
            right_value = int(input("Enter right value: "))
            parentNode.right = Node(right_value)
            self.nodePlacer(parentNode.right)
    
    
    def node_populater(self, arr):
        node = self.root
        index = 0
        while index < len(arr):
            node.left = Node(arr[index])
            index +=1
            if index < len(arr):
                node.right = Node(arr[index])
            index +=1
            
            
    def prettyDisplay(self, parentNode, level):
        if parentNode == None:
            return # as soon as we dont have anything print that many tabs and pring number at the end
        
        # find the last right node
        self.prettyDisplay(parentNode.right, level+1)
        
        
        if level != 0:
            for i in range(level-1):
                print("|\t", end="")
            print(f"|------>{parentNode.val}")
        else:
            print(parentNode.val)
         
        # left in that level 
        self.prettyDisplay(parentNode.left, level+1)

# https://leetcode.com/problems/symmetric-tree/

    def isSymmetric(self, root):
        return self.isSymmetric_helper(root.left, root.right)
        
    def isSymmetric_helper(self, left, right):
        if left == None and right == None:
            return True
        
        if (left == None and right != None) or (right == None and left != None):
            return False
        
        if left.val != right.val:
            return False
        
        if not self.isSymmetric_helper(left.left, right.right): # if false is returned , return false directly or else continue
            return False

        return self.isSymmetric_helper(left.right, right.left)
    

bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.isSymmetric(bt.root))