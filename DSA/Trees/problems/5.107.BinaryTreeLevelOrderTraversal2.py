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

    def levelOrderBottom(self, root):
        q = deque()
        q.append(root)
        out_put=[]
        
        self.levelOrderBottom_helper(q, out_put)
    
        return out_put
    
    def levelOrderBottom_helper(self, q, out_put):
        if not len(q):
            return
        
        lvl_size = len(q)
        cur_lvl_nums =[]
        for _ in range(lvl_size):
            node = q.popleft()
            cur_lvl_nums.append(node.val)
            if node.left != None:
                q.append(node.left)
            
            if node.right != None:
                q.append(node.right)
        
        self.levelOrderBottom_helper(q, out_put)
        
        out_put.append(cur_lvl_nums)

    def levelOrderBottom2(self, root):
        q = deque()
        q.append(root)
        out_put =[]
        while len(q):
            levelSize = len(q)
            curr_lvl_nums = []
            for _ in range(levelSize):
                node = q.popleft()
                curr_lvl_nums.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                    
            out_put.append(curr_lvl_nums)
        return out_put[::-1]
    
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.levelOrderBottom(bt.root))
print(bt.levelOrderBottom2(bt.root))
                  