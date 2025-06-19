from typing import List

# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        groups = 0
        cur = -float("inf")
        for n in nums:
            if n > cur + k:
                groups += 1
                cur = n
        return groups
