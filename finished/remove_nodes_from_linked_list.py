from typing import Optional, Tuple

# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
          if not node:
            return node, -1
          
          nx, _max = helper(node.next)
          if node.val >= _max:
            node.next = nx
            return node, node.val
          else:
            return nx, _max
          
        return helper(head)[0]