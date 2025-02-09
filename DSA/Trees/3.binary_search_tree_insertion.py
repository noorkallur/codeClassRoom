class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert_value(self, val):
        self.root = self.insert_value_helper(self.root, val) 
        return
        
    def insert_value_helper(self, parentNode, val):
        if parentNode == None:
            new_node = Node(val)
            return new_node
        
        if val <= parentNode.val:
            parentNode.left = self.insert_value_helper(parentNode.left, val)
        else:
            parentNode.right = self.insert_value_helper(parentNode.right, val)

        return parentNode # after attaching, we return the same parentNode
    
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
            print(f"|------>{parentNode.val}")
        else:
            print(parentNode.val)
         
        # left in that level 
        self.prettyDisplay_helper(parentNode.left, level+1)  
        
        
bst = BST()
bst.insert_value(10)
bst.insert_value(8)
bst.insert_value(5)
bst.insert_value(15)
bst.insert_value(7)
bst.prettyDisplay()