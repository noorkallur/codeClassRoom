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
  
    def zigzagLevelOrder_noor(self, root):
        q = deque()
        q.append(root)
        output =[]
        rev = False
        while len(q):
            curr_lvl_nums = []
            lvl_size = len(q)
            for _ in range(lvl_size):
                node = q.popleft()
                curr_lvl_nums.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:    
                    q.append(node.right)
            #zig zag
            if rev == True:
                output.append(curr_lvl_nums[::-1])
            else:
                output.append(curr_lvl_nums)
            
            rev = not rev
                
        return output
    
    def zigzagLevelOrder_dev(self, root):
        q = deque()
        q.append(root)
        output =[]
        rev = False
        while len(q):
            curr_lvl_nums = []
            lvl_size = len(q)
            for _ in range(lvl_size):
                if rev == False: # add and remove zig zag
                    node = q.popleft()
                    curr_lvl_nums.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:    
                        q.append(node.right)
                else:
                    node = q.pop()
                    curr_lvl_nums.append(node.val)
                    if node.right:    
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                        
            output.append(curr_lvl_nums)
            rev = not rev # change the order
                
        return output
    
    
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.zigzagLevelOrder(bt.root))
print(bt.zigzagLevelOrder_dev(bt.root))