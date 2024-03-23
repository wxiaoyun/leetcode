# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node, n):
            if node == None:
                return 0
            
            length = helper(node.next, n) + 1
            
            if length == n + 1:
                node.next = node.next.next
            
            return length
        
        dummy_head = ListNode(None, head)

        helper(dummy_head, n)
        return dummy_head.next