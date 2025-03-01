# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

class Solution:
    #  everything in a is smaller than or equals to everything in b
    # def findMedianTotalOrderArrays(self, a, b):
    #     if len(a) == len(b): # a and b same length, just take the average of the edge elements
    #         return (a[-1] + b[0]) / 2

    #     total_len = len(a) + len(b)
    #     is_even = total_len % 2 == 0
    #     if is_even:
    #         index = total_len // 2
    #     else:
    #         index = total_len / 2

    #     if is_even:
    #         if index >= len(a):
    #             return (b[index - len(a)] + b[index - len(a) - 1]) / 2
    #         else:
    #             return (a[index] + a[index - 1]) / 2
        
    #     else: # is odd
    #         index = math.floor(index)
    #         if index >= len(a):
    #             return b[index - len(a)]
    #         else:
    #             return a[index]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        # Ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A
        
        total_len = len(A) + len(B)
        half = total_len // 2
        is_even = total_len % 2 == 0

        l = 0
        r = len(A) - 1

        while True:
            m_a = (r - l) // 2 + l
            m_b = half - m_a - 2

            al = A[m_a] if m_a >= 0 else -math.inf
            bl = B[m_b] if m_b >= 0 else -math.inf
            ar = A[m_a+1] if m_a+1 < len(A) else math.inf
            br = B[m_b+1] if m_b+1 < len(B) else math.inf

            if al <= br and bl <= ar:
                if is_even:
                    return (max(al, bl) + min(ar, br)) / 2
                else:
                    return min(ar, br)
            elif al > br:
                r = m_a - 1
            else: # bl > ar
                l = m_a + 1
