# https://leetcode.com/problems/unique-paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        # m >= n
        tmp = [0] * n
        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for c in range(n):
                tmp[c] = dp[c]
                if c > 0:
                    tmp[c] += tmp[c - 1]
            dp, tmp = tmp, dp
        return dp[-1]
