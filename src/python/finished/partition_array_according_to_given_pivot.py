from typing import List

# https://leetcode.com/problems/partition-array-according-to-given-pivot


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        eq = []
        more = []

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                eq.append(n)
            else:
                more.append(n)

        less.extend(eq)
        less.extend(more)
        return less
