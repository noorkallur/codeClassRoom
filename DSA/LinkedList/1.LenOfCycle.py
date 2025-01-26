
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fastP = head
        slowP = head
        len = 0
        while fastP != None and fastP.next != None:
            slowP = slowP.next
            fastP = fastP.next.next 
            if slowP == fastP: # we know cycle exists
                # take temp and iterate till you reach the same point
                temp = slowP
                while True: # alternative to a do while loop
                    temp = temp.next
                    len += 1
                    if temp == slowP: # reached the slow pointer, break
                        break
    
        return len