# https://leetcode.com/problems/linked-list-cycle-ii/description/
# https://youtu.be/70tx7KcMROc?si=ue0N275uRPGGrtNX
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fastP = head
        slowP = head
        while fastP != None and fastP.next != None:
            slowP = slowP.next
            fastP = fastP.next.next
            if fastP == slowP: # found cycle
                break
            else:
                return None #no cycle return none
        
        #using floyd's algorithm find the start of the cycle
        leftP = head
        while slowP != leftP: # when they cross eachother that means its the start of the cycle
            leftP = leftP.next
            slowP = slowP.next
        return leftP