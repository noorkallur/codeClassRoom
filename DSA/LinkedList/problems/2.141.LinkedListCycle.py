# https://leetcode.com/problems/linked-list-cycle/
# https://youtu.be/70tx7KcMROc?si=_suMe7cyaY7uxiAD
# Definition for singly-linked list.

# as we know fast and slow will eventually meet at some point in a cycle, we use that technique to solve it
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fastP = head
        slowP = head

        while fastP != None and fastP.next != None:
            slowP = slowP.next
            fastP = fastP.next.next 
            if slowP == fastP:
                return True
        
        return False