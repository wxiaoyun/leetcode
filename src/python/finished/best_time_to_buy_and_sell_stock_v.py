from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        IDLE = 0
        BUY = 1
        SELL = 2

        def compute(dp: dict, prices: List[int], i: int, k: int, state: bool) -> int:
            if k < 0:
                return -float("inf")
            if i >= len(prices):
                if state != IDLE:
                    return -float("inf")
                return 0

            key = (i, k, state)
            if key in dp:
                return dp[key]

            best = -float("inf")
            p = prices[i]

            if state == IDLE:
                # we can either do nothing, buy or sell

                # do nothing
                best = max(best, compute(dp, prices, i + 1, k, state))

                # buy
                best = max(best, -p + compute(dp, prices, i + 1, k, SELL))

                # sell
                best = max(best, p + compute(dp, prices, i + 1, k, BUY))

            elif state == BUY:
                # we can either do nothing or buy

                # do nothing
                best = max(best, compute(dp, prices, i + 1, k, state))

                # buy
                best = max(best, -p + compute(dp, prices, i + 1, k - 1, IDLE))

            else:
                assert state == SELL
                # we can either do nothing or sell

                # do nothing
                best = max(best, compute(dp, prices, i + 1, k, state))

                # sell
                best = max(best, p + compute(dp, prices, i + 1, k - 1, IDLE))

            dp[key] = best
            return best

        return compute({}, prices, 0, k, IDLE)
