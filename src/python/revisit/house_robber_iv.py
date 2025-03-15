from typing import List

# https://leetcode.com/problems/house-robber-iv/


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = min(nums), max(nums)

        while l < r:
            m = l + (r - l) // 2

            robs = 0
            i = 0
            while i < N:
                if nums[i] <= m:
                    robs += 1
                    i += 2
                else:
                    i += 1

            if robs >= k:
                r = m
            else:
                l = m + 1

        return l
