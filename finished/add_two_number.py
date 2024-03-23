# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2

        dummy = ListNode(None)
        result = dummy

        while curr1 or curr2:
            num1, num2 = 0, 0
            c = carry # carry from previous addition

            if curr1:
                num1 = curr1.val
                curr1 = curr1.next
            if curr2:
                num2 = curr2.val
                curr2 = curr2.next
            
            total = num1 + num2 + c
            if total < 10:
                n = ListNode(total)
                carry = 0
            else:
                n = ListNode(total % 10)
                carry = 1
            
            result.next = n
            result = n
        
        if carry == 1:
            result.next = ListNode(1)
        
        return dummy.next
        