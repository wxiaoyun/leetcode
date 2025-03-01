# https://leetcode.com/problems/merge-nodes-in-between-zeros

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()

        prev = dummy_head
        cur_node = head.next
        cur_sum = 0
        while cur_node:
            if cur_node.val == 0:
                node = ListNode(cur_sum)
                cur_sum = 0
                prev.next = node
                prev = node
            else:
                cur_sum += cur_node.val
            cur_node = cur_node.next

        return dummy_head.next