from typing import List

# https://leetcode.com/problems/minimum-distance-to-the-target-element/


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        INF = 1 << 32
        ans = INF
        for i, n in enumerate(nums):
            if n != target:
                continue
            if abs(i - start) < ans:
                ans = abs(i - start)
        return ans
