# https://leetcode.com/problems/copy-list-with-random-pointer/


from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {}
        old_to_copy[None] = None
        current = head

        while current != None:
            old_to_copy[current] = Node(current.val)
            current = current.next
        
        current = head
        while current != None:
            old = current
            copy = old_to_copy[old]

            copy.next = old_to_copy[old.next]
            copy.random = old_to_copy[old.random]

            current = current.next
        
        return old_to_copy[head]