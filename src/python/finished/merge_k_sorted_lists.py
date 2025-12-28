import heapq
from typing import List, Optional

# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [(n.val, i, n.next) for i, n in enumerate(lists) if n is not None]
        heapq.heapify(pq)

        head = ListNode()
        cur = head
        while pq:
            v, tiebreaker, nxt = heapq.heappop(pq)
            tmp = ListNode(v)
            cur.next = tmp
            cur = tmp

            if nxt is not None:
                heapq.heappush(pq, (nxt.val, tiebreaker, nxt.next))

        return head.next
