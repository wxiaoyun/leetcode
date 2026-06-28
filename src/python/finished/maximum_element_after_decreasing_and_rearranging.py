from typing import List

# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        prev = 0
        for i, n in enumerate(arr):
            prev = min(prev + 1, n)
        return min(prev, arr[-1])
