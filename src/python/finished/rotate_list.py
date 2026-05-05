from typing import Optional

# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        cur = head
        l = 1
        while cur.next is not None:
            cur = cur.next
            l += 1

        cur.next = head
        k = k % l

        cur = head
        for _ in range(l - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head
