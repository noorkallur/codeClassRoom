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
        
    def flatten(self, root):
        def flatten_helper(root):
            if root == None:
                return
            
            bin_list.append(root)
            flatten_helper(root.left)
            flatten_helper(root.right)
        
        bin_list= []
        flatten_helper(root)
        node_itr = root
        for node in bin_list[1:]:
            node_itr.right = node
            node_itr.left = None
            node_itr =  node_itr.right
            
    def shift(self, node):
        temp = node.right
        node.right = node.left
        if node.right:
            node.right.right = temp 
        node.left = None
            
    def flatten2(self, root):
        
        def shift(node):
            if node.left == None:
                return
            temp = node.right
            node.right = node.left
            node.left = None
            if temp:
                node_itr = node.right
                while node_itr.right:
                    node_itr = node_itr.right
                node_itr.right = temp 
            
        def straighten(node):
            if node == None:
                return
            
            straighten(node.left)
            straighten(node.right)
            shift(node)
            
        straighten(root)

        
        
        
        
bst = BST()
bst.insert_value(6)
bst.insert_value(2)
bst.insert_value(15)
bst.insert_value(3)
bst.insert_value(4)
bst.insert_value(16)
print("pre#####")
bst.prettyDisplay()
bst.flatten2(bst.root)
print("post#####")
bst.prettyDisplay()



