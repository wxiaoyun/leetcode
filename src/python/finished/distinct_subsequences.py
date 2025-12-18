# https://leetcode.com/problems/distinct-subsequences/

# O(m * n) space optimised bottom up
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [0] * (m + 1)
        dp[0] = 1
        tmp = [0] * (m + 1)
        tmp[0] = 1

        # dp[i][j] = number of distinct subsequences of s[:i] which equals t[:j]
        # dp[i][j] =
        #  + dp[i - 1][j]
        #  + if (s[i] == s[j]) dp[i - 1][j - 1] else 0

        for i in range(1, n + 1):
            schr = s[i - 1]
            for j in range(1, m + 1):
                tchr = t[j - 1]

                tmp[j] = dp[j]
                if schr == tchr:
                    tmp[j] += dp[j - 1]

            dp, tmp = tmp, dp

        return dp[-1]


# O(m * n) recursion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def compute(dp: dict, i: int, j: int) -> int:
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            key = (i, j)
            if key in dp:
                return dp[key]

            ways = 0

            # skip
            ways += compute(dp, i + 1, j)

            # take
            if s[i] == t[j]:
                ways += compute(dp, i + 1, j + 1)

            dp[key] = ways
            return ways

        return compute({}, 0, 0)
