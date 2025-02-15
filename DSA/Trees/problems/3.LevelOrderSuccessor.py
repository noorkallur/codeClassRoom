# google question
# https://youtu.be/9D-vP-jcc-Y?t=2048&si=X1WzdnHPOEzaQTIB
# Given a tree find the next node of the given target node
# look at the 3.LevelOrderSuccessor.png to understand better
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

    
    def level_order_successor(self, root, target):
        q = deque()
        q.append(root)
        
        while len(q):
            node = q.popleft()
                
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

            if target == node.val:
                if len(q):
                    return q.popleft().val
    
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.level_order_successor(bt.root, 3))
print(bt.level_order_successor(bt.root, 9))
print(bt.level_order_successor(bt.root, 20))
print(bt.level_order_successor(bt.root, 15))
print(bt.level_order_successor(bt.root, 7))
        