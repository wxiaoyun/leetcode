from typing import List


# https://leetcode.com/problems/ones-and-zeros/


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros

            for i in reversed(range(zeros, m + 1)):
                for j in reversed(range(ones, n + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
