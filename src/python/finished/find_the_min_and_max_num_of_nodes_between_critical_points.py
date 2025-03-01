# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points


# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        _min, _max = float('inf'), -float('inf')
        far_idx, close_idx = None, None

        def is_critical(prev: ListNode, cur: ListNode) -> bool:
            if not prev or not cur or not cur.next:
                return False
            
            left = prev.val
            mid = cur.val
            right = cur.next.val

            if ((left > mid and right > mid) or (left < mid and right < mid)):
                return True
            else:
                return False

        prev = None
        cur = head
        idx = 0
        while cur:
            is_cur_critical = is_critical(prev, cur)

            if far_idx and far_idx != idx and is_cur_critical:
                _max = max(_max, idx-far_idx)
            if close_idx and close_idx != idx and is_cur_critical:
                _min = min(_min, idx-close_idx)
            
            # Only set far once
            if not far_idx and is_cur_critical:
                far_idx = idx
            if is_cur_critical:
                close_idx = idx

            prev = cur
            cur = cur.next
            idx += 1

        return [-1, -1] if _min > _max else [_min, _max]
        
        