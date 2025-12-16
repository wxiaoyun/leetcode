from typing import List

# https://leetcode.com/problems/coin-change-ii/


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def ways(dp: dict, amount: int, coins: List[int], i: int) -> int:
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            key = (amount, i)
            if key in dp:
                return dp[key]

            c = coins[i]
            nways = ways(dp, amount - c, coins, i) + ways(dp, amount, coins, i + 1)
            dp[key] = nways
            return nways

        return ways({}, amount, coins, 0)
