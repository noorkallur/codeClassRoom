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

    
    def rightSideView(self, root):
        q = deque()
        q.append(root)
        out_put = []
        
        while len(q):
            lvl_size = len(q)
            for i in range(lvl_size):
                node = q.popleft()
                if i == lvl_size - 1: # take the last num of the level
                    out_put.append(node.val)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return out_put
    
    # i am proud of this solution
    def rightSideView_with_no_space(self, root):
        level = 0
        output = []
        self.rightSideView_with_no_space_helper(root, level, output)
        return output
        
    def rightSideView_with_no_space_helper(self, root, level, output):
        if root == None:
            return
        if len(output) <= level:
            output.append(root.val) # if arr is out of the bounds then append
        else:
            output[level] = root.val # update the latest value
        self.rightSideView_with_no_space_helper(root.left, level+1, output)
        self.rightSideView_with_no_space_helper(root.right, level+1, output)

        
        
    
    
bt = BinaryTree()
bt.prettyDisplay(bt.root, 0)
print(bt.rightSideView(bt.root))
print(bt.rightSideView_with_no_space(bt.root))
