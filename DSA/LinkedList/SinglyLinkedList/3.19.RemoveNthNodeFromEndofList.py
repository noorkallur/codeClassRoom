# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
import LinkedList as ll

obj = ll.LinkedList()
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.printLinkedList() #creating a linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(head:ll.Node, n):
    # Solution 1 : 
    # find the length
    # length - n = remaing elements (4 - 2 = 2 elements remaining) + 1 will give us the element we want to delet. coincedentally that also becomes our index
    # remove that element at that index
    
    # Solution 2: clever and fast
    # using two pointer method and using n as the distance apart if n = 2 l = head, r = l.next.next (one in beteween) why as we incremnt with +1 to each other , in the end l is going to land at desired position
    # clever tecnique: use dummy in the begining and point l to dummy, so we dont have to use prev node to delete the desired node and return dmmy.next
    
    dummy = Node(0)
    dummy.next = head # d->1->2->3->4
    left = dummy
    right = head
    # point the right to the distance apart from left
    while n != 0 and right != None:
        right = right.next
        n -=1
    # if n is 2, right should be pointing to 3 and at this point left to dummy
    
    #traverse to the prev node of the desired removal node
    while right != None:
        left = left.next
        right = right.next
    
    # remove the next node left
    left.next = left.next.next
    
    #printing the the ll   
    iterate_ll = dummy.next
    ll = []
    while iterate_ll != None:
        ll.append(iterate_ll.data)
        iterate_ll = iterate_ll.next
        
    print(ll)
    

removeNthFromEnd(obj.head, 5)
    