class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, val):
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            return
        
        curr_last = self.head
        while curr_last.next != None:
            curr_last = curr_last.next
        
        curr_last.next = newNode
    
    
    def insertAtBegining(self, val):
        new_head = Node(val)
        if self.head == None:
            self.head = new_head
            
        curr_head = self.head
        new_head.next = curr_head
        self.head = new_head
    
    
    def insertAtIndex(self, index, val):
        if index == 0:
            self.insertAtBegining(val)
            return
        
        new_node = Node(val)
        prev_node = self.head
        position = 0
        #find the prev node right before we place our new node
        while prev_node!=None and position + 1 != index:
            prev_node=prev_node.next
            position = position + 1
            
        if prev_node != None:
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print(f"index not found {index}")
            
    def updateAtIndex(self, index, val):
        position = 0
        curr_node = self.head
        while curr_node != None and position != index:
            curr_node = curr_node.next
            position += 1
        
        if curr_node != None:
            curr_node.data = val
        else:
            print(f"{index} index not present")
            
                   
    def deleteFromEnd(self):
        if self.head == None:
            # no data in linked list
            return
        if self.head.next == None:
            #head is the last node
            self.head = None
            return
        #find the last node
        currentNode = self.head
        while currentNode.next.next != None:
            currentNode = currentNode.next
        
        currentNode.next = None
       
        
    def deleteFromBegining(self):
        if self.head == None:
            print(f"Nothing to delete")
            return
        self.head = self.head.next
        
        
    def deleteNodeAtIndex(self, index):
        if index == 0:
            self.deleteFromBegining()
            return
        
        position = 0
        prev_node = self.head
        while prev_node != None and position + 1 != index:
            prev_node = prev_node.next
            position = position + 1
        
        prev_node.next = prev_node.next.next
        
    
    def deleteNodeOfVal(self, val):
        currnode = self.head
        position = 0
        while currnode != None:
            if currnode.data == val:
                self.deleteNodeAtIndex(position)
                return
            currnode = currnode.next
            position +=1
        
        print(f"No node with value {val}")
        
    
    def reverseLinkedList(self):
        curr_node = self.head
        prevnode = None
        
        while curr_node != None:
            temp_next = curr_node.next
            curr_node.next = prevnode
            prevnode = curr_node
            curr_node = temp_next
        
        self.head = prevnode
    
          
    def printLinkedList(self):
        current_node = self.head
        ll = []
        while current_node != None:
            ll.append(current_node.data)
            current_node = current_node.next
            
        print(ll)
        
if __name__ == "__main__":        
    obj = LinkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtIndex(2, 3)
    obj.insertAtEnd(5)
    obj.printLinkedList()
    obj.deleteNodeOfVal(3)
    obj.printLinkedList()
    obj.reverseLinkedList()
    obj.printLinkedList()

