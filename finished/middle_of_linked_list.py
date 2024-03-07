# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_len(self, head: Optional[ListNode]) -> int:
        l = 0
        current = head

        while current != None:
            l += 1
            current = current.next
        
        return l

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.find_len(head)
        mid = l // 2
        current = head

        while mid > 0:
            mid -= 1
            current = current.next
        
        return current
