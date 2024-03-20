# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_minus_one = None
        b_plus_one = None

        current = list1
        n_th = 0

        while True:
            if n_th == (a - 1):
                a_minus_one = current
            if n_th == (b + 1):
                b_plus_one = current
                break

            current = current.next
            n_th += 1
        
        # set a-1 to point to start of list2
        a_minus_one.next = list2

        current = list2

        while current.next != None:
            current = current.next
        
        # set end of list2 to point to b+1
        current.next = b_plus_one

        return list1