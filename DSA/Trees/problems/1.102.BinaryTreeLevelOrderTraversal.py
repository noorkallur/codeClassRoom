from collections import deque 

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        root_node = input("Insert ROOT node: ")
        self.root = Node(root_node)
        self.nodePlacer(self.root)
        
    def nodePlacer(self, parentNode):
        left = input(f"Do you want to place left of {parentNode.val} (y/n): ")
        if left == "y":
            left_value = input("Enter left value: ")
            parentNode.left = Node(left_value)
            self.nodePlacer(parentNode.left)
            
        right = input(f"Do you want to place right of {parentNode.val} (y/n): ")
        if right == "y":
            right_value = input("Enter right value: ")
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
       
    def levelOrder(self):
        q = deque()
        q.append(self.root)
        res =[[self.root.val]]
        while len(q):
            levelSize = len(q)
            ls = []
            for _ in range(levelSize):
                node = q.popleft()
                ls.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                    
            res.append(ls)
        return res
                 
        
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.levelOrder())