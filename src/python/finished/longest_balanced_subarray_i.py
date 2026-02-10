from typing import List

# https://leetcode.com/problems/longest-balanced-subarray-i


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best = 0
        for l in range(len(nums)):
            evens, odds = set(), set()
            for i in range(l, len(nums)):
                n = nums[i]
                if n & 1 == 0:
                    evens.add(n)
                else:
                    odds.add(n)
                if len(evens) == len(odds):
                    best = max(best, i - l + 1)
        return best
