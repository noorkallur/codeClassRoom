# https://leetcode.com/problems/add-two-numbers/description/
import LinkedList as ll
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
obj = ll.LinkedList()
obj.insertAtEnd(2)
obj.insertAtEnd(4)
obj.insertAtEnd(3)
obj.printLinkedList() #creating a linked list

obj2 = ll.LinkedList()
obj2.insertAtEnd(5)
obj2.insertAtEnd(6)
obj2.insertAtEnd(4)
obj2.printLinkedList() #creating a linked list

obj = ll.LinkedList()
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.insertAtEnd(9)
obj.printLinkedList() #creating a linked list

obj2 = ll.LinkedList()
obj2.insertAtEnd(9)
obj2.insertAtEnd(9)
obj2.insertAtEnd(9)
obj2.printLinkedList() #creating a linked list




def addTwoNumbers(l1:Node, l2:Node):
    ans = curr = Node(0)
    carry = 0
    while l1!= None or l2 != None or carry != 0:
        dig1 = l1.data if l1 != None else 0
        dig2 = l2.data if l2 != None else 0
        curr.next = Node((dig1 + dig2 + carry)%10  )
        carry = (dig1 + dig2 + carry)//10
        curr = curr.next
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    
    # return ans.next
    #printing   
    iterate_ll = ans.next
    ll = []
    while iterate_ll != None:
        ll.append(iterate_ll.data)
        iterate_ll = iterate_ll.next
        
    print(ll)

addTwoNumbers(obj.head, obj2.head)