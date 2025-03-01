# Definition for singly-linked list.
from typing import Optional

# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: Optional[ListNode]) -> bool:
          if not node:
            return False
          
          carry = helper(node.next)

          dub = node.val * 2
          if carry:
            dub += 1
          node.val = dub % 10
          return (dub // 10) > 0
        
        carry = helper(head)
        if carry:
          return ListNode(val=1, next=head)
        else:
          return head


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
          num *= 10
          num += cur.val
          cur = cur.next
        
        num *= 2

        if num == 0:
          return ListNode(val=0)

        cur = None
        while num:
          rem = num % 10
          num = num // 10
          cur = ListNode(val=rem, next=cur)
        return cur
