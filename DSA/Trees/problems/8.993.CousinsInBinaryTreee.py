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


    # I came up this solution
    def isCousins(self, root:Node, x:int ,y:int):
        def areBothPresent(q):
            lvl_nums=[]
            while len(q):
                node = q.popleft()
                lvl_nums.append(node.val)
                
            if x in lvl_nums and y in lvl_nums:
                return True
            else:
                return False
            
        q = deque()
        q.append(root)
        one_tar_found = False
        while len(q):
            lvl_size = len(q)
            lvl_nums = []
            for _ in range(lvl_size):
                node = q.popleft()
                lvl_nums.append(node.val)
                if node.left:
                    q.append(node.left)
                    if node.left.val == x or node.left.val == y:
                        one_tar_found = True
                        continue # skip to make sure same parent is skipped 
                if node.right:
                    q.append(node.right)
                    if node.right.val == x or node.right.val == y:
                        one_tar_found = True

            # now we know have the lvl nodes in q, check if we have both x and y are target
            if one_tar_found:
                return areBothPresent(q)
                
        
        return False
    
    
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.isCousins(bt.root, 2, 3)) # false
print(bt.isCousins(bt.root, 4, 3)) # false
print(bt.isCousins(bt.root, 4, 5)) # false
print(bt.isCousins(bt.root, 4, 6)) # true
print(bt.isCousins(bt.root, 4, 7)) # true
                