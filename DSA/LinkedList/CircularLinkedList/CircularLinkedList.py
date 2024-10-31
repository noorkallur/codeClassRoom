class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class CircLL:
    
    def __init__(self):
        self.head = None
        
    
    def insert_at_end(self, val):
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.tail.next = newNode
        self.tail = newNode
    
    def printcll(self):
        curr_node = self.head
        cll = []
        while curr_node.next != self.head:
            cll.append(curr_node.val)
            curr_node = curr_node.next
        
        cll.append(self.tail.val)
        
        print(cll)


cll = CircLL()

cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.printcll()