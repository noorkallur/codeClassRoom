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
        prev_head = self.head
        self.head = Node(val)
        self.head.next = prev_head
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
print(f"Qsize: {q.qsize}")
print(q.pop())
print(f"Qsize: {q.qsize}")
print(q.pop())
print(f"Qsize: {q.qsize}")
print(q.pop())
print(f"Qsize: {q.qsize}")
print(q.pop())
q.printQ()

    