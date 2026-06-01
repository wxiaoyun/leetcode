from typing import List

# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse=True)

        total_cost = 0
        for i, c in enumerate(cost):
            if i % 3 != 2:
                total_cost += c
        return total_cost
