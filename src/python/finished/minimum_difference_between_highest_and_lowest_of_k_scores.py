from typing import List

# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return min(nums[i] - nums[i - k + 1] for i in range(k - 1, len(nums)))
