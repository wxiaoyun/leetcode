class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        dp_up = [1] * m
        dp_down = [1] * m
        dp_up_tmp = [-1] * m
        dp_down_tmp = [-1] * m
        MOD = int(1e9) + 7

        for _ in range(2, n + 1):
            summ = 0
            for i in range(m):
                dp_up_tmp[i] = summ
                summ += dp_down[i]
                summ %= MOD

            summ = 0
            for i in range(m - 1, -1, -1):
                dp_down_tmp[i] = summ
                summ += dp_up[i]
                summ %= MOD

            dp_down, dp_down_tmp = dp_down_tmp, dp_down
            dp_up, dp_up_tmp = dp_up_tmp, dp_up

        return (sum(dp_down) + sum(dp_up)) % MOD


# TLE
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # dp[<i, prev, inc>]
        MOD = int(1e9) + 7
        dp = {}

        def compute(i: int, prev: int, inc: bool) -> int:
            if i == n:
                return 1

            key = (i, prev, inc)
            if key in dp:
                return dp[key]

            ans = 0
            for nxt in range(l, r + 1):
                if nxt == prev:
                    continue

                inc_new = prev < nxt
                if inc_new == inc:
                    continue

                ans += compute(i + 1, nxt, inc_new)
                ans %= MOD
            dp[key] = ans
            return ans

        total = 0
        for i in range(l, r + 1):
            for j in range(l, r + 1):
                if i == j:
                    continue
                total += compute(2, j, j > i)
                total %= MOD
        return total
