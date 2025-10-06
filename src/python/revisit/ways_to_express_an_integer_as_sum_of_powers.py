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


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = int(1e9 + 7)

        # key = <n, next_base>
        def compute(dp: dict, n: int, next_base: int, x: int) -> int:
            key = (n, next_base)
            if key in dp:
                return dp[key]

            if n == 0:
                return 1

            next_pow = next_base**x
            if next_pow > n:
                return 0

            ways = 0

            # use next_base
            ways += compute(dp, n - next_pow, next_base + 1, x)
            ways %= MOD

            # skip next_base
            ways += compute(dp, n, next_base + 1, x)
            ways %= MOD

            dp[key] = ways
            return ways

        return compute({}, n, 1, x)
