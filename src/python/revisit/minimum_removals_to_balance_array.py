from typing import List

# https://leetcode.com/problems/minimum-removals-to-balance-array


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        best = 0
        for i in range(n):
            a = nums[i]
            for j in range(i + best, n):
                b = nums[j]
                if b / a > k:
                    break
                best = max(best, j - i + 1)

        return n - best
