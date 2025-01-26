# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# for test cases look at the leetcode 
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head:Node):
    #first we need a hash_map of old node to new node(random is nothing but index of old node)
    #creating a new list with val same as old
    # while assigne random, from map we now know for what old node is the new node 
    if head == None :
        return head
    old_to_new_map = {}

    # hash_map old to new node
    currNode = head
    while currNode != None:
        old_to_new_map[currNode] = Node(currNode.val) # created the new nodes not linked them yet
        currNode = currNode.next
    
    # random assigning and linking of the new list
    currNode = head
    while currNode != None:
        # link the next of new list
        old_to_new_map[currNode].next = old_to_new_map.get(currNode.next) # map[None] == key error, hence using get() as map.get(None) == None
        # new.random = old_to_new[old.random] (random is nothing but index of old node)
        old_to_new_map[currNode].random = old_to_new_map.get(currNode.random)
        currNode = currNode.next
    
    return old_to_new_map[head]
