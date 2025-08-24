# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_sum = [0] * N  #
        prefix_sum[0] = nums[0]
        posfix_sum = [0] * N
        posfix_sum[-1] = nums[-1]

        for i in range(1, N):
            prefix_sum[i] = 0 if nums[i] == 0 else prefix_sum[i - 1] + 1
            j = N - 1 - i
            posfix_sum[j] = 0 if nums[j] == 0 else posfix_sum[j + 1] + 1

        best = 0
        if N > 1:
            best = max(posfix_sum[1], prefix_sum[-2])
        for i in range(1, N - 1):
            best = max(best, prefix_sum[i - 1] + posfix_sum[i + 1])

        return best
