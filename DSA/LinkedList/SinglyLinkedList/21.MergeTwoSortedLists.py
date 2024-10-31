import LinkedList as ll

list1 = ll.LinkedList()
list1.insertAtEnd(1)
list1.insertAtEnd(2)
list1.insertAtEnd(4)
list1.printLinkedList() #creating a linked list

list2 = ll.LinkedList()
list2.insertAtEnd(1)
list2.insertAtEnd(4)
list2.insertAtEnd(5)
list2.printLinkedList() #creating a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # [1, 2, 4]
    # [1, 4, 5]
    # mll = dummy->1->1->2->4->4->5
    # return mll.next (to avoid dummy node)
    def mergeTwoLists(self, list1:ll.Node, list2:ll.Node):
        mergedll= Node(0) #use to enter all ther merged data
        mergedll_head_reference = mergedll#used as reference to return at the end 
        while list1 != None and list2 != None:
            if list1.data < list2.data:
                mergedll.next = list1
                list1 = list1.next
                
            else:
                mergedll.next = list2
                list2 = list2.next
                
            mergedll = mergedll.next
            
        #after all the merging anything left in any of the lists?   
        if list1:
            mergedll.next = list1
        elif list2:
            mergedll.next = list2
                  
        #printing the merged the ll
        mergedll_head_reference = mergedll_head_reference.next  
        ll = []
        while mergedll_head_reference != None:
            ll.append(mergedll_head_reference.data)
            mergedll_head_reference = mergedll_head_reference.next
            
        print(ll)
                     
        
        
mll = Solution()
mll.mergeTwoLists(list1.head, list2.head)