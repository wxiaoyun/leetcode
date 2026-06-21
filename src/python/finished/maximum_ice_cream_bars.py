from typing import List

# https://leetcode.com/problems/maximum-ice-cream-bars


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)

        cnt = [0] * (mx + 1)
        for c in costs:
            cnt[c] += 1

        n_ic = 0
        for v in range(1, len(cnt)):
            c = cnt[v]

            # if coins - v * c >= 0
            # if coins  >= v * c
            # if coins / v >=  * c

            n = min(coins // v, c)
            n_ic += n
            coins -= n * v
            if coins == 0:
                break

        return n_ic
