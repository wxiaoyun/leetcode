from typing import List


# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos = set(k for k in nums if k > 0)
        if len(pos) > 0:
            return sum(pos)
        return max(nums)
