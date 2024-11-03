# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mid_of_ll(self, node: ListNode):
        slow = node
        fast = node.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        rightP = slow.next
        slow.next = None
        return rightP

    def merge(self, lp: ListNode, rp: ListNode):
        mll = ListNode()
        ref_mll = mll

        while lp != None and rp != None:
            if lp.val < rp.val:
                mll.next = lp
                lp = lp.next
            else:
                mll.next = rp
                rp = rp.next
            mll = mll.next   
            
        if lp != None:
            mll.next = lp

        if rp != None:
            mll.next = rp
        
        return ref_mll.next

    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        rightP = self.mid_of_ll(head)

        left = self.sortList(head)
        right = self.sortList(rightP)

        ans = self.merge(left, right)
        return ans
        
        