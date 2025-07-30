from typing import List

# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description


# O(n) time
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        best = 0
        best_num = -1
        i = 0
        while i < N:
            n = nums[i]
            llen = 0
            while i < N and n == nums[i]:
                llen += 1
                i += 1
            if n == best_num:
                best = max(best, llen)
            elif n > best_num:
                best = llen
                best_num = n
        return best
