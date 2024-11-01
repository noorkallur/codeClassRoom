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
            newNode.next = self.head
            return
        
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        
        curr_node.next = newNode
        newNode.next = self.head
    
    def delete_at_index(self, index):
        
        if index == 0:
            if self.head == self.head.next: #if there is only one element
                self.head = None
            else:
                # set tail.next to new head
                curr_node = self.head
                while curr_node.next != self.head:
                    curr_node = curr_node.next
                    
                curr_node.next =  self.head.next # setting the tail to new head
                self.head = self.head.next # making the next element as new head
                
            return
        
        curr_node = self.head
        count = 0
        while count < index - 1: #iterate till prev node
            curr_node = curr_node.next
            count += 1
            if curr_node.next == self.head:
                return "out of range"
        
        curr_node.next = curr_node.next.next


    def delete_value(self, value):
        
        if value == self.head.val:
            if self.head == self.head.next:
                self.head = None
            else:
                # set tail.next to new head
                curr_node = self.head
                while curr_node.next != self.head:
                    curr_node = curr_node.next
                    
                curr_node.next =  self.head.next # setting the tail to new head
                self.head = self.head.next # making the next element as new head
            return

        curr_node = self.head
        while curr_node.next != self.head:
            if curr_node.next.val == value:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next
        
        return "value not found"

            
            
        
    def printcll(self):
        cll = []
        if self.head == None:
            print(cll)
            return
        curr_node = self.head
        while curr_node.next != self.head:
            cll.append(curr_node.val)
            curr_node = curr_node.next
        
        cll.append(curr_node.val)
        
        print(cll)


cll = CircLL()

cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.printcll()
cll.delete_at_index(0)
cll.printcll()
cll.delete_at_index(2)
cll.printcll()
cll.delete_at_index(0)
cll.printcll()
cll.delete_at_index(0)
cll.printcll()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.printcll()
cll.delete_value(3)
cll.printcll()
cll.delete_value(4)
cll.printcll()
cll.delete_value(1)
cll.printcll()
cll.delete_value(2)
cll.printcll()