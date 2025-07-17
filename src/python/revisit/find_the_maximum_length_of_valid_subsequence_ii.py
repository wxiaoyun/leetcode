# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for n in nums:
            md = n % k
            for j in range(k):
                dp[j][md] = dp[md][j] + 1
        return max(max(ls) for ls in dp)
