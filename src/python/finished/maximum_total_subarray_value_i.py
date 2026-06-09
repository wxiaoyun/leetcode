from typing import List

# https://leetcode.com/problems/maximum-total-subarray-value-i


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
