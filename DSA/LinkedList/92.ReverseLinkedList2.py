# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #does not work for edge cases
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverese_ll(head: ListNode):
            current_node = head
            prevnode = None
            while current_node != None:
                tempNext = current_node.next
                current_node.next = prevnode
                prevnode = current_node
                current_node = tempNext
            return prevnode

        if left == right:
            return head
        lpos = None
        curr = head
        pos = 1
        while left > 1 or right > 1:
            if pos == left-1:
                lpos = curr
            curr = curr.next
            pos += 1

            if pos == right:
                break
        
        # swap lpos and curr
        if lpos == None and curr.next == None:
            return reverese_ll(head)
        else:
            print("noor")
            if lpos == None:
                print("noor1")
                head = curr.next
                head.next = lpos
                curr.next = None
                return reverese_ll(head)
            elif curr.next == None:
                print("noor2")
                curr.next = lpos
                head = lpos.next
                lpos.next = None
                return reverese_ll(head)
            else:
                print("noor3")   
                head = curr.next
                head.next = lpos.next
                curr.next = lpos
                lpos.next = None
                print(head)
                return reverese_ll(head)
            

        #reverse the whole linked list



        
        