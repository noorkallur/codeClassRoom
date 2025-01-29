class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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


    def reverseBetween(self, left, right):
        """
            Reverses a sublist of a linked list from position `left` to `right`.

            Parameters:
            left (int): The starting position of the sublist to be reversed (1-indexed).
            right (int): The ending position of the sublist to be reversed (1-indexed).

            Returns:
            None: The linked list is modified in place.

            Description:
            This function reverses the nodes of a linked list from position `left` to `right`. 
            It uses a dummy node to handle edge cases where the reversal starts at the head of the list. 
            The function iterates through the list, reversing the pointers of the nodes between `left` and `right`. 
            After the reversal, it reconnects the reversed sublist with the rest of the list.

            Edge Cases:
            - If `left` is equal to `right`, the list remains unchanged.
            - If `left` or `right` are out of bounds (i.e., less than 1 or greater than the length of the list), the function should handle these cases appropriately:
                - If `left` < 1, it should be set to 1.
                - If `right` > length of the list, it should be set to the length of the list.
            - If the list is empty, the function should return immediately without making any changes.
            - If `left` is greater than `right`, the function should return immediately as it is an invalid range.
            
            Example:
            Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and left = 2, right = 4,
            the function will modify the list to 1 -> 4 -> 3 -> 2 -> 5.
        """
        
        if left == right:
            return
        
        dummy_head = Node(None)  # Dummy node to handle edge cases
        dummy_head.next = self.head
        
        curr_node = dummy_head
        position = 0
        prev_node = None
        left_side = None
        reverse_end = None
        
        while curr_node:
            if position == left:  # Mark the start of the reversal
                left_side = prev_node
                reverse_end = curr_node
            
            if position == right:  # End of the reversal
                rend = curr_node.next
                curr_node.next = prev_node  # Reverse the current node, this is the final reversal
                
                # Connect the reversed sublist with the rest of the list
                if rend and left != 1:
                    left_side.next = curr_node
                    reverse_end.next = rend
                elif rend and left == 1:
                    reverse_end.next = rend
                    self.head = curr_node
                elif not rend and left != 1:
                    left_side.next = curr_node
                    reverse_end.next = None
                else:
                    self.head = curr_node
                    reverse_end.next = None
                
                return  # Exit as we have completed the reversal
            
            next_node = curr_node.next
            if position >= left:  # Reverse the nodes between left and right
                curr_node.next = prev_node
            prev_node = curr_node    
            position += 1
            curr_node = next_node
 
    def reverseBetween(self, left, right):
        '''
        this logic is simpler
        '''
        if not self.head or left == right:
            return

        dummy = Node(None)
        dummy.next = self.head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        print(f"prev {prev.data}")
        cur = prev.next
        # insert one at the left side each run
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            self.print_linked_list()
        return dummy.next
# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)
# ll1.add_node_at_end(4) 
# ll1.add_node_at_end(5)

# ll1.print_linked_list()
# ll1.reverseBetween(3, 4) 
# ll1.print_linked_list()

# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)
# ll1.add_node_at_end(4) 
# ll1.add_node_at_end(5)

# ll1.print_linked_list()
# ll1.reverseBetween(2, 4) 
# ll1.print_linked_list()   

# ll1 = LinkedList()
# ll1.add_node_at_end(5)

# ll1.print_linked_list()
# ll1.reverseBetween(1, 1) 
# ll1.print_linked_list()        
        

# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)

# ll1.print_linked_list()
# ll1.reverseBetween(1, 2) 
# ll1.print_linked_list()   


# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)

# ll1.print_linked_list()
# ll1.reverseBetween(2, 3) 
# ll1.print_linked_list()   


# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)

# ll1.print_linked_list()
# ll1.reverseBetween(3, 3) 
# ll1.print_linked_list()   


# ll1 = LinkedList()
# ll1.add_node_at_end(1)
# ll1.add_node_at_end(2)
# ll1.add_node_at_end(3)
# ll1.add_node_at_end(4) 
# ll1.add_node_at_end(5)

# ll1.print_linked_list()
# ll1.reverseBetween(4, 5) 
# ll1.print_linked_list() 
        
        