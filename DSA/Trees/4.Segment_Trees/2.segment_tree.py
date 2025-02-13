class Node:
    def __init__(self, data, start_index, end_index):
        self.data = data
        self.start = start_index
        self.end = end_index
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.root = self.create_segment_tree(arr, 0, len(arr)-1)
        
    def create_segment_tree(self, arr, start, end):
        if start == end:
            leaf = Node(arr[start], start, end)
            return leaf
        
        mid = (start + end)//2
        node = Node(None, start, end)
        node.left = self.create_segment_tree(arr, start, mid)
        node.right = self.create_segment_tree(arr, mid+1, end)
        
        node.data = node.left.data + node.right.data
        
        return node

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
            print(f"|------>{parentNode.data}({parentNode.start},{parentNode.end})")
        else:
            print(f"{parentNode.data}({parentNode.start},{parentNode.end})")
         
        # left in that level 
        self.prettyDisplay_helper(parentNode.left, level+1)  
        
        
    def insert_at_index(self, index, val):
        self.root = self.insert_at_index_helper(index, val, self.root)
    
    def insert_at_index_helper(self, index, val, node):
        if node.start == index and node.end == index:
            node.data = val
            return node
        
        if node.start == node.end:
            return node
        
        if index >= node.start and index <= node.end:
            node.left = self.insert_at_index_helper(index, val, node.left)
            node.right = self.insert_at_index_helper(index, val, node.right)
        
        node.data = node.left.data + node.right.data
        
        return node

    
    def sum_of_range_inclusive(self, start, end):
        return self.sum_of_range_inclusive_helper(start, end, self.root)
    
    def sum_of_range_inclusive_helper(self, start, end, node):
        
        if node.start > end or node.end < start: # check if its completely out of range, is nstart is ahead oi end or nenf is behind nstart
            return 0
        
        if node.start >= start and node.end <= end: # check if node.start and node.end is inside query range
            return node.data
        
        sum = self.sum_of_range_inclusive_helper(start, end, node.left) + self.sum_of_range_inclusive_helper(start, end, node.right)
        
        return sum
        

arr = [3, 8, 7, 6, -2, -8, 4, 9]
sgt = SegmentTree(arr)
sgt.prettyDisplay()
print(sgt.sum_of_range_inclusive(2,6))
print(sgt.sum_of_range_inclusive(4,6))
print(sgt.sum_of_range_inclusive(0,7))
print(sgt.sum_of_range_inclusive(1,6))
# sgt.insert_at_index(3, 10)
# print("#######################################################")
# sgt.prettyDisplay()