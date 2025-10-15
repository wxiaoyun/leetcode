from typing import List

# https://leetcode.com/problems/adjacent-increasing-subarrays-detection/


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        best = 1
        prev_l, l = 0, 1
        for i in range(1, len(nums) + 1):
            prev = nums[i - 1]
            cur = nums[i] if i < len(nums) else -float("inf")

            if cur > prev:
                l += 1
            else:
                k = min(prev_l, l)
                best = max(best, k, l // 2)
                prev_l = l
                l = 1

        return best
