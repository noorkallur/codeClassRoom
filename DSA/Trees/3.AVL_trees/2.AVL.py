# if you dont understand AVL watch https://youtu.be/CVA85JuJEn0?t=2542&si=2pJuD0UU1JUtlbJD

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 0
        
class AVL:
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
            return -1
        else:
            return node.height 
            
    def insert_node(self, value):
        self.root = self.insert_node_helper(self.root, value)
        
    def insert_node_helper(self, node, value):
        if node == None:
            return Node(value)
        
        if value <= node.val:
            node.left = self.insert_node_helper(node.left, value) 
        else:
            node.right = self.insert_node_helper(node.right, value) 
        
        node.height = max(self.height(node.left), self.height(node.right) ) + 1
        
        return self.balance(node)
    
    def balance(self, node):
        # check if the tree is UNBALANCED (left heavy)
        if self.height(node.left) - self.height(node.right) > 1:
            # check if left is heavy of c for LEFT LEFT
            if self.height(node.left.left) - self.height(node.left.right) > 0:
                # move p to right
                return self.rotate_right(node)        
           
            # LEFT RIGHT case
            if self.height(node.left.left) - self.height(node.left.right) < 0:
                # move c/g to left
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)    
         
        # check if the tree is UNBALANCED (right heavy)
        if self.height(node.left) - self.height(node.right) < -1:   
            # check if the right side is heavy of c for RIGHT RIGHT
            if self.height(node.right.left) - self.height(node.right.right) < 0:
                # move p to left
                return self.rotate_left(node)
            
            # RIGHT LEFT case
            if self.height(node.right.left) - self.height(node.right.right) > 0:
                # move c to right
                node.right = self.rotate_right(node.right)
                # move p to left
                return self.rotate_left(node)
        
        return node
    
    def rotate_right(self, p):
        # draw this case first or check the tree_rotation.png
        c = p.left
        t = c.right
        c.right = p
        p.left = t
        
        # how to adjust heigt, if we notice height will only be change for c and p not all draw it if you want
        # first adjust for p because it is in the bottom
        p.height = max(self.height(p.left), self.height(p.right)) + 1
        # now update c which is on the top
        c.height = max(self.height(c.left), self.height(c.right)) + 1
        
        return c    
    
    def rotate_left(self, c):
        # why i have put c as arg instead of p.. tbh it does not matter i am just following the same diagram to re purpose and visualize rotating left
        p = c.right
        t = p.left
        p.left = c
        c.right = t
        
        # how to adjust heigt, if we notice height will only be change for c and p not all nodes, draw it if you want
        # first adjust for c because it is in the bottom
        c.height = max(self.height(c.left), self.height(c.right)) + 1
        # now update p which is on the top
        p.height = max(self.height(p.left), self.height(p.right)) + 1
        return p
    
    
avl = AVL()
for i in range(0, 1000):
    avl.insert_node(i)
    
# avl.prettyDisplay()
print(avl.height(avl.root))