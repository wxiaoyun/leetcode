# https://leetcode.com/problems/count-the-number-of-ideal-arrays


# Memory limit exceeded
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # since the next number must be divisible by the previous number,
        # the array is monotonically non-decreasing

        MOD = 10**9 + 7
        dp = {}

        def compute(i: int, prev: int) -> int:
            if i == n - 1:
                return maxValue // prev

            key = (i, prev)
            if key in dp:
                return dp[key]

            res = 0
            for nx in range(prev, maxValue + 1, prev):
                res = (res + compute(i + 1, nx)) % MOD

            dp[key] = res
            return res

        return compute(0, 1)
