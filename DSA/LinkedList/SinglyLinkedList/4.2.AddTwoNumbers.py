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


# # this is how is solved it later, pretty long but it works if i had spent some time i would have probally done the same as above
# def addTwoNumbers(self, l1, l2):
#     curr_node = Node(None)
#     ref = curr_node
#     lend = 0

#     while l1 and l2:
#         add_val = (l1.data + l2.data)%10
#         print(f"add{add_val}")
#         print(f"lend{lend}")
#         newNode = Node(add_val + lend)
#         lend = (l1.data + l2.data + lend)//10
#         curr_node.next = newNode
#         curr_node = curr_node.next
#         l1 = l1.next
#         l2 = l2.next

#     while l1:
#         print(f"add{(l1.data + lend)%10}")
#         newNode = Node((l1.data + lend)%10)
#         print(f"lend{lend}")
#         lend = (l1.data+lend)//10
#         curr_node.next = newNode
#         curr_node = curr_node.next
#         l1 = l1.next
        
#     while l2:
#         print(f"add{(l2.data + lend)%10}")
#         newNode = Node((l2.data + lend)%10)
#         lend = (l2.data + lend)//10
#         print(f"lend{lend}")
#         curr_node.next = newNode
#         curr_node = curr_node.next
#         l2 = l2.next
        

#     newNode = Node(lend)
#     curr_node.next = newNode
        
#     self.head = ref.next