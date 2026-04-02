from typing import List

# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        INF = 1 << 32
        dp = [[[-INF] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][2] = coins[0][0]
        dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                left = i > 0
                top = j > 0

                coins_delta = coins[i][j]

                for k in range(3):
                    neut = k > 0

                    if left:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + coins_delta)

                        if neut and coins_delta < 0:
                            dp[i][j][k - 1] = max(dp[i][j][k - 1], dp[i - 1][j][k])

                    if top:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + coins_delta)

                        if neut and coins_delta < 0:
                            dp[i][j][k - 1] = max(dp[i][j][k - 1], dp[i][j - 1][k])

        return max(dp[-1][-1])
