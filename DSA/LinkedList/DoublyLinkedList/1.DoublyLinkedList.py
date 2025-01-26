class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, val):
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            return
        
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        
        newNode.prev = curr_node    
        curr_node.next = newNode
        self.tail = curr_node.next

    def insert_at_index(self, val, index):
        newNode = Node(val)
        curr_node  = self.head
        
        while curr_node != None and index > 0:
            curr_node = curr_node.next
            index = index - 1
        
        newNode.prev = curr_node.prev
        curr_node.prev.next = newNode
        newNode.next = curr_node
        curr_node.prev = newNode
            
    def delete_at_index(self, index):
        curr_node = self.head
        
        while curr_node != None and index > 0:
            curr_node = curr_node.next
            index = index - 1    
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
      
        
    def delete_at_end(self):
        tail_node = self.tail
        
        tail_node = tail_node.prev
        tail_node.next = None
    

    def print_dll(self):
        curr_node = self.head
        while curr_node != None:
            if curr_node.prev != None:
                prev_val = curr_node.prev.val
            else:
                prev_val = None
            print(f"{prev_val}<-{curr_node.val}")
            curr_node = curr_node.next
            
dll = DoublyLinkedList()

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.print_dll()
dll.insert_at_index(8, 2)
dll.print_dll()
dll.delete_at_index(2)
print(f"result")
dll.print_dll()
