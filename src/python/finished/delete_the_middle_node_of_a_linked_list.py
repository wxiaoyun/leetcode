from typing import Optional

# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        slow_prev = None

        while True:
            if not fast.next:
                break
            fast = fast.next

            assert slow is not None
            slow_prev = slow
            slow = slow.next

            if not fast.next:
                break
            fast = fast.next

        if not slow_prev:
            return slow.next

        slow_prev.next = slow.next
        return head
