import LinkedList as ll

obj = ll.LinkedList()
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.printLinkedList() #creating a linked list

class Solution:
    def reverseList(self, head:ll.Node):
        current_node = head
        prevnode = None
        while current_node != None:
            tempNext = current_node.next
            current_node.next = prevnode
            prevnode = current_node
            current_node = tempNext
         
        #printing the reversed the ll   
        iterate_ll = prevnode
        ll = []
        while iterate_ll != None:
            ll.append(iterate_ll.data)
            iterate_ll = iterate_ll.next
            
        print(ll)
                     
        
        
rll = Solution()
rll.reverseList(obj.head)