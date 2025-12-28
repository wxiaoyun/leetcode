from typing import Optional

# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k(node: Optional[ListNode], k: int, builder: Optional[ListNode]):
    if k == 0:
        return builder

    nxt = node.next
    node.next = builder
    return reverse_k(nxt, k - 1, node)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for _ in range(k):
            if cur is None:
                return head
            cur = cur.next

        next_group = self.reverseKGroup(cur, k)
        new_head = reverse_k(head, k, next_group)
        return new_head
