# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        pows = []
        i = 1
        while i**x <= n:
            pows.append(i**x)
            i += 1

        MOD = int(1e9 + 7)
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in pows:
            for num in reversed(range(p, n + 1)):
                dp[num] = (dp[num] + dp[num - p]) % MOD

        return dp[n]
