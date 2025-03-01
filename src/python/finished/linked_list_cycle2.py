# https://leetcode.com/problems/linked-list-cycle/description/
# This is a reattempt of the problem.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head
        slow = head

        while (slow.next != None and fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True
        
        return False
