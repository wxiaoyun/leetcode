from typing import List

# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        mx = 0
        for i in range(N):
            a = nums[i]
            b = nums[(i + 1) % N]
            mx = max(mx, abs(a - b))
        return mx
