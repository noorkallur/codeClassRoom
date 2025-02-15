# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# https://youtu.be/9D-vP-jcc-Y?t=3316&si=l9WoNIAVZBxcNMfW
from collections import deque 

class Node:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None
        self.next = None
        
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
            
    def prettyDisplay(self, parentNode, level):
        if parentNode == None:
            return # as soon as we dont have anything print that many tabs and pring number at the end
        
        # find the last right node
        self.prettyDisplay(parentNode.right, level+1)
        
        if level != 0:
            for i in range(level-1):
                print("|\t", end="")
            next_node = parentNode.next
            if next_node!=None:
                next_node = next_node.val
            print(f"|------>{parentNode.val}({next_node})")
        else:
            print(f"{parentNode.val}({parentNode.next})")
        # left in that level 
        self.prettyDisplay(parentNode.left, level+1)
    
    # I came up with both solutions
    def connect(self, root):
        q = deque()
        q.append(root)
        while len(q):
            lvl_size = len(q)
            for i in range(lvl_size):
                node = q.popleft()
                
                if i != lvl_size - 1:
                    node.next = q[0]
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
     
    # no extra space, please draw it out                
    def connect_with_no_space(self, root):
        self.connect_with_no_space_helper(root)
        return root
        
        
    def connect_with_no_space_helper(self, root):
        if root == None:
            return
        
        if root.left:
            root.left.next = root.right
            
        if root.right and root.next:
            root.right.next = root.next.left
        
        self.connect_with_no_space(root.left)
        self.connect_with_no_space(root.right)
        
    
bt = BinaryTree()
bt.connect_with_no_space(bt.root)
bt.prettyDisplay(bt.root, 0)
            