from typing import List

# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        longest = 1

        i = 1
        while i < N:
            streak = 1
            while i < N and nums[i] > nums[i-1]:
                streak += 1
                i += 1
            longest = max(longest, streak)
            i += 1

        i = 1
        while i < N:
            streak = 1
            while i < N and nums[i] < nums[i-1]:
                streak += 1
                i += 1
            longest = max(longest, streak)
            i += 1
                
        return longest