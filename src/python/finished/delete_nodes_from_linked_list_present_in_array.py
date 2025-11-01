from typing import List, Optional

# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        dh = ListNode(next=head)
        prev = dh
        cur = dh.next
        while cur is not None:
            if cur.val in nums:
                cur = cur.next
                continue

            prev.next = cur
            prev = cur
            cur = cur.next
            prev.next = None

        return dh.next
