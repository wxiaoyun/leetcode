import math
from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prefix_min = [math.inf] * len(prices)
        # prefix_min[0] = prices[0]
        # postfix_max = [-math.inf] * len(prices)
        # postfix_max[-1] = prices[-1]

        # for i in range(1, len(prices)):
        #     prefix_min[i] = min(prefix_min[i-1], prices[i])
        #     postfix_max[-i-1] = max(postfix_max[-i], prices[-i-1])

        # cur = -math.inf
        # for i in range(len(prices)):
        #     cur = max(cur, postfix_max[i] - prefix_min[i])

        # return cur
        min_price_seen = math.inf
        cur_max = 0

        for p in prices:
            min_price_seen = min(min_price_seen, p)
            cur_max = max(cur_max, p - min_price_seen)

        return cur_max


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Base case
        if len(prices) <= 1:
            return 0

        # preprocess the maximum element reading from the right
        # max is monotonically non-increasing
        max = [0] * len(prices)
        max[-1] = prices[-1]

        for i in range(1, len(prices)):
            j = len(prices) - 1 - i
            if prices[j] > max[j + 1]:
                max[j] = prices[j]
            else:
                max[j] = max[j + 1]

        # attempts to find the maximum profit
        maxProfit = 0
        for i in range(0, len(prices)):
            profit = max[i] - prices[i]
            if profit < 0:
                continue  # no profit
            elif profit > maxProfit:
                maxProfit = profit
        return maxProfit
