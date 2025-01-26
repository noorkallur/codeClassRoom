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
    
    def insert_via_recurison_helper(self, index, val, curr_node):
        if curr_node.next == None:
            return
        
        if index == 1:
            newNode = Node(val)
            newNode.next = curr_node.next
            curr_node.next = newNode
            return
        
        self.insert_via_recurison_helper(index - 1, val, curr_node.next)
        
    def insert_via_recurison(self, index, val):
        if index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode 
            return
        
        self.insert_via_recurison_helper(index, val, self.head)
        
          
    def printLinkedList(self):
        current_node = self.head
        ll = []
        while current_node != None:
            ll.append(current_node.data)
            current_node = current_node.next
            
        print(ll)

# I wrote this after some time, check the below
class LinkedList_2:
    def __init__(self):
        self.head = None
    
    def print_linked_list(self):
        itr =self.head
        ll =[]
        while itr:
            ll.append(itr.data)
            itr =itr.next
        print(ll)
        
    def add_node_at_end(self, nodeVal):
        
        if self.head == None:
            self.head = Node(nodeVal)
            return
        
        nodeItr = self.head
        while nodeItr.next:
            nodeItr = nodeItr.next
        
        nodeItr.next = Node(nodeVal)
        
    def remove_node_at_end(self):
        if self.head == None:
            print(f"Error: Empty Linked list")
            return

        itr = self.head
        
        while itr.next.next:
            itr = itr.next
        
        itr.next = None
        
    def insert_at_begining(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        
        ref_head = self.head
        self.head = Node(val)
        self.head.next = ref_head
            
        
    def insert_at_index(self, index, val):
        if index == 0:
            self.insert_at_begining(val)
            return
        
        curr_idx = 1
        itr = self.head
        
        while itr.next:
            if curr_idx == index:
                new_node = Node(val)
                new_node.next = itr.next
                itr.next = new_node
                return
            curr_idx +=1
            itr = itr.next
        
        print(f"Error: index {index} is not found")
        
    def update_at_index(self, index, val):
        
        curr_index = 0
        itr = self.head
        
        while itr:
            if curr_index == index:
                itr.data =val
                return
            
            curr_index += 1
            itr =itr.next
            
        print(f"Error: index {index} is not found")
        
    def remove_from_begining(self):
        if self.head == None:
            print(f"Error: Nothing to delete")
            return 
        self.head = self.head.next   
        
    def delete_node_at_index(self, index):
        if index == 0:
            return self.remove_from_begining()
        curr_idx = 1
        itr = self.head
        while itr.next:
            if curr_idx == index:
                itr.next = itr.next.next
                return
            curr_idx +=1
            itr = itr.next
        
        print(f"Error: Index {index} is not found")
    
    def reverse_linked_list(self):
        prev_node = None
        itr = self.head
        while itr.next:
            next_node = itr.next
            itr.next = prev_node
            prev_node = itr
            itr = next_node
        
        itr.next = prev_node
        
        self.head = itr

    def insert_via_recursion_at_index(self, index, val):
        if index == 0:
            return self.insert_at_begining(val)
        
        def helperFunction(itr:Node, curr_idx):
            while itr:
                if curr_idx == index:
                    new_node = Node(val)
                    new_node.next = itr.next
                    itr.next = new_node
                    return
                itr = itr.next
                return helperFunction(itr, curr_idx+1)
                
        itr = self.head
        curr_idx = 1
        helperFunction(itr, curr_idx)

 
     
if __name__ == "__main__":        
    obj = LinkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtIndex(2, 3)
    obj.insertAtEnd(5)
    obj.printLinkedList()
    obj.insert_via_recurison(3, 4)
    obj.printLinkedList()
    obj.insert_via_recurison(0, 0)
    obj.printLinkedList()
    
    print("new linked list")
    ll1 = LinkedList_2()
    ll1.add_node_at_end(1)
    ll1.add_node_at_end(2)
    ll1.add_node_at_end(3)
    ll1.add_node_at_end(4)
    ll1.insert_at_begining(5)
    ll1.insert_at_index(4, 6)
    ll1.update_at_index(0, 0)
    ll1.update_at_index(4, 4)
    ll1.update_at_index(5, 5)
    ll1.update_at_index(5, 5)
    ll1.print_linked_list()


