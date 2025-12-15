from typing import List

# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descents = len(prices)

        prices.append(-1)
        prev, streak = -1, 0
        for p in prices:
            if prev - 1 == p:
                streak += 1
                prev = p
                continue

            n_choose_two = streak * (streak - 1) // 2
            descents += n_choose_two

            streak = 1
            prev = p

        return descents
