# https://leetcode.com/problems/soup-servings/


import random
import math
from typing import Callable, Tuple


class Solution:
    def soupServings(self, n: int) -> float:
        m = math.ceil(n / 25)
        if m >= 200:
            return 1.0

        deltas = [
            (4, 0),
            (3, 1),
            (2, 2),
            (1, 3),
        ]

        m1 = m + 1
        dp = [[0] * m1 for _ in range(m1)]
        dp[0] = [1] * m1
        dp[0][0] = 1 / 2

        for a in range(1, m1):
            for b in range(1, m1):
                for da, db in deltas:
                    dp[a][b] += dp[max(0, a - da)][max(0, b - db)]
                dp[a][b] = dp[a][b] / 4

        return dp[m][m]


# Monto Carlo, TLE
class Solution:
    def soupServings(self, n: int) -> float:
        def monte_carlo(n: int, cond: Callable) -> bool:
            a = [100, 75, 50, 25]
            b = [0, 25, 50, 75]
            na, nb = n, n

            while True:
                idx = random.randint(0, 3)
                na -= a[idx]
                nb -= b[idx]

                stop, hit = cond(na, nb)
                if stop:
                    break

            return 1 if hit else 0

        def simulate(
            n: int, cond: Callable, step: int = 1000, eps: float = 1e-5
        ) -> float:
            count = step
            total = sum(monte_carlo(n, cond) for _ in range(step))

            while True:
                prev_avg = total / count

                total += sum(monte_carlo(n, cond) for _ in range(step))
                count += step
                cur_avg = total / count

                if abs(cur_avg - prev_avg) < eps:
                    return cur_avg

        def a_used_before_b(na: int, nb: int) -> Tuple[bool, bool]:
            stop = na <= 0 or nb <= 0
            hit = na <= 0 and nb > 0
            return stop, hit

        def used_together(na: int, nb: int) -> Tuple[bool, bool]:
            stop = na <= 0 or nb <= 0
            hit = na <= 0 and nb <= 0
            return stop, hit

        return simulate(n, a_used_before_b) + (simulate(n, used_together) / 2)
