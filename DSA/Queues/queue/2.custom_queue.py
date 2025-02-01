class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class CustomQueue:
    def __init__(self):
        self.head = None
        self.qsize = 0
        
    def printQ(self):
        curr_itr = self.head
        ls = []
        while curr_itr:
            ls.append(curr_itr.val)
            curr_itr = curr_itr.next
        print(ls)

    def push(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            
        curr_node.next = Node(val)
        self.qsize += 1
        

    def pop(self):
        if self.head == None:
            return
        dequeud = self.head.val
        self.head = self.head.next
        self.qsize -= 1
        return dequeud
    

    
q = CustomQueue()

q.push(1)    
q.push(2)    
q.push(3)
q.printQ()
print(q.pop())
q.printQ()
q.push(4)
print(q.pop())
q.printQ()
q.push(5)
print(q.pop())
q.printQ()
print(q.pop())
q.printQ()

    