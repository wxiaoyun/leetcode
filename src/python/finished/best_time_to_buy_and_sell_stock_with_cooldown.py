from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # states:
        # - Hold nothing
        # - Hold a stock of price x
        # - Sold a stock with cooldown

        # from previous state
        # - Do nothing:
        # - Buy a stock if previous state is hold nothing or cooldown finished
        # - Sell a stock if previous state is holding a stock

        FREE = 0
        HOLDING_STOCK = 1

        def compute(dp: dict, ty: int, i: int) -> int:
            key = (ty, i)
            if key in dp:
                return dp[key]

            if i >= len(prices):
                return 0

            best = -float("inf")
            if ty == FREE:
                # do nothing
                best = max(best, compute(dp, ty, i + 1))

                # buy
                best = max(best, compute(dp, HOLDING_STOCK, i + 1) - prices[i])

            else:
                assert ty == HOLDING_STOCK

                # do nothing
                best = max(best, compute(dp, ty, i + 1))

                # sell
                best = max(best, prices[i] + compute(dp, FREE, i + 2))

            dp[key] = best
            return best

        return compute({}, 0, 0)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # states:
        # - Hold nothing
        # - Hold a stock of price x
        # - Sold a stock with cooldown

        # from previous state
        # - Do nothing:
        # - Buy a stock if previous state is hold nothing or cooldown finished
        # - Sell a stock if previous state is holding a stock

        FREE = 0
        HOLDING_STOCK = 1

        def compute(dp: dict, ty: int, payload: int, i: int) -> int:
            key = (ty, payload, i)
            if key in dp:
                return dp[key]

            if i >= len(prices):
                return 0

            best = -float("inf")
            if ty == FREE:
                cooldown = payload

                # do nothing
                best = max(best, compute(dp, ty, max(0, cooldown - 1), i + 1))

                # buy
                if cooldown == 0:
                    best = max(
                        best, compute(dp, HOLDING_STOCK, prices[i], i + 1) - prices[i]
                    )

            else:
                assert ty == HOLDING_STOCK
                stock_val = payload

                # do nothing
                best = max(best, compute(dp, ty, stock_val, i + 1))

                # sell
                if prices[i] > stock_val:
                    best = max(best, prices[i] + compute(dp, FREE, 1, i + 1))

            dp[key] = best
            return best

        return compute({}, 0, 0, 0)
