# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

import math
from typing import List


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
