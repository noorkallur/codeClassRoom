class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root =None
        
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
        
    def insert_node(self, value):
        self.root = self.insert_node_helper(self.root, value)
        
    def insert_node_helper(self, parenNode, value):
        if parenNode == None:
            return Node(value)
        
        if value <= parenNode.val:
            parenNode.left = self.insert_node_helper(parenNode.left, value)
        else:
            parenNode.right = self.insert_node_helper(parenNode.right, value)
            
        return parenNode
    
    def pre_order_traversals(self):
        self.pre_order_traversals_helper(self.root)
        
    def pre_order_traversals_helper(self, node):
        if node == None:
            return
        
        print(node.val)
        self.pre_order_traversals_helper(node.left)
        self.pre_order_traversals_helper(node.right)
        
    def in_order_traversals(self):
        self.in_order_traversals_helper(self.root)
    
    def in_order_traversals_helper(self, node):
        if node == None:
            return

        self.in_order_traversals_helper(node.left)
        print(node.val)
        self.in_order_traversals_helper(node.right)
        
    def post_order_traversals(self):
        self.post_order_traversals_helper(self.root)

    def post_order_traversals_helper(self, node):
        if node == None:
            return
        
        self.post_order_traversals_helper(node.left)
        self.post_order_traversals_helper(node.right)
        print(node.val)
        
        
bst = BST()
bst.insert_node(15)
bst.insert_node(10)
bst.insert_node(20)
bst.insert_node(5)
bst.insert_node(12)
bst.insert_node(8)
# bst.prettyDisplay()
bst.post_order_traversals()