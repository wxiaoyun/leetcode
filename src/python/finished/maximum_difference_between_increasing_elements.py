# https://leetcode.com/problems/maximum-difference-between-increasing-elements


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = float("inf")
        best = -1
        for n in nums:
            if n > mn:
                best = max(best, n - mn)
            mn = min(mn, n)
        return best
