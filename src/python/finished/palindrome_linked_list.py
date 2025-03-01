# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def helper(l: Optional[ListNode], next: Optional[ListNode]):
            if next:
                current = next.val
                next = next.next
                return helper(ListNode(current, l), next)

            # we have reached the end of the list
            current = head
            while current:
                if current.val != l.val:
                    return False

                current = current.next
                l = l.next

            return True

        return helper(None, head)
