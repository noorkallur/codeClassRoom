import LinkedList as ll

obj = ll.LinkedList()
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.printLinkedList() #creating a linked list

obj2 = ll.LinkedList()
obj2.insertAtEnd(1)
obj2.insertAtEnd(2)
obj2.insertAtEnd(3)
obj2.insertAtEnd(4)
obj2.insertAtEnd(5)
obj2.printLinkedList() #creating a linked list

def reorderList(head:ll.Node):
    # Initial idea:
    # reverse a list
    #insert element of the reversed list one by one till we have the same node
    # make that same node.next = null
    # :(
    # failure reason: I thought keeping dummy = head will have the copy of the ll itself but since after reversing no copy of original survied hence failure
    
    # Dev solution
    # use fast and slow pointer to find the mid way of the inked list
    # reverse the second half of the linked list
    # merge the both halfs one by one left first right next
    
    # find mid way
    slowP = head
    fastP = head
    while fastP != None and fastP.next != None:
        slowP = slowP.next
        fastP = fastP.next.next
    
    # Reverse the second half of the list
    secondll = slowP.next
    prevnode = None
    while secondll != None:
        temp_next = secondll.next
        secondll.next = prevnode
        prevnode = secondll
        secondll = temp_next
    
    # point to null for first half
    slowP.next = None 
    
    # Merge the 2 halves
    secondll = prevnode
    firstll = head
    
    while firstll != None and secondll != None:
        temp_next = secondll.next
        secondll.next = firstll.next
        firstll.next = secondll
        
        secondll = temp_next
        firstll = firstll.next.next
        
    #printing  head 
    iterate_ll = head
    ll = []
    while iterate_ll != None:
        ll.append(iterate_ll.data)
        iterate_ll = iterate_ll.next
        
    print(ll)
    
reorderList(obj.head)
reorderList(obj2.head)
