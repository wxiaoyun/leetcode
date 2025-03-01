from typing import List

# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg = 0
        pos = 0
        best = 0
        for n in nums:
            if n >= 0:
                pos += n
                neg = min(0, neg + n)
                best = max(best, pos, abs(neg))
            else:  # n < 0
                neg += n
                pos = max(0, pos + n)
                best = max(best, pos, abs(neg))
        return best

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        N = len(nums)
        best = 0
        for i in range(N):
            s = 0
            for j in range(i, N):
                s += nums[j]
                best = max(best, abs(s))
        return best
