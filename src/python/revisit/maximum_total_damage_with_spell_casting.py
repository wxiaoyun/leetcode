from typing import List
from collections import Counter

# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power_cnt = Counter(power)
        powers = sorted(power_cnt.items())
        n = len(powers)
        dp = [0] * n

        best = 0
        j = 0
        for i in range(n):
            while j < i and powers[j][0] < powers[i][0] - 2:
                best = max(best, dp[j])
                j += 1
            p, f = powers[i]
            dp[i] = p * f + best
        return max(dp)
