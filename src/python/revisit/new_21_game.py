# https://leetcode.com/problems/new-21-game/


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k <= 0:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        # dp[i] = P(Obtain i points)
        # dp[i] = sum k from 1...=maxPts (
        #   dp[i - k] / maxPts if k < i
        # )

        frac = 1 / maxPts
        interval_sum = 1
        for i in range(1, n + 1):
            dp[i] = interval_sum * frac

            if i < k:
                interval_sum += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                interval_sum -= dp[i - maxPts]

        return sum(dp[k:])
