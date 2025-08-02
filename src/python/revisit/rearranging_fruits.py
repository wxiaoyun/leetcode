from typing import List
from collections import Counter

# https://leetcode.com/problems/rearranging-fruits/


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)

        t1 = []  # excess items from basket1 pending exchange to basket2
        t2 = []  # excess items from basket2 pending exchange to basket1
        keys = set(cnt1.keys())
        keys.update(cnt2.keys())
        # print(keys)
        for f in keys:
            c1, c2 = cnt1[f], cnt2[f]
            if c1 == c2:
                continue

            total = c1 + c2
            if total & 1 == 1:
                # odd count
                return -1

            avg = (c1 + c2) // 2
            if c1 > c2:
                t1.append([f, c1 - avg])
            else:
                t2.append([f, c2 - avg])

        t1.sort()
        t2.sort()

        swap_via_min_cost = 2 * min(keys)
        t1l, t1r = 0, len(t1) - 1
        t2l, t2r = 0, len(t2) - 1
        cost = 0
        while t1l <= t1r:
            choice_a = t1[t1l][0]
            choice_b = t2[t2l][0]

            if choice_a < choice_b:
                deduct = min(t1[t1l][1], t2[t2r][1])
                cost += min(choice_a, swap_via_min_cost) * deduct

                if t1[t1l][1] - deduct == 0:
                    t1l += 1
                else:
                    t1[t1l] = (t1[t1l][0], t1[t1l][1] - deduct)

                if t2[t2r][1] - deduct == 0:
                    t2r -= 1
                else:
                    t2[t2r] = (t2[t2r][0], t2[t2r][1] - deduct)
            else:
                deduct = min(t2[t2l][1], t1[t1r][1], swap_via_min_cost)
                cost += min(choice_b, swap_via_min_cost) * deduct

                if t2[t2l][1] - deduct == 0:
                    t2l += 1
                else:
                    t2[t2l] = (t2[t2l][0], t2[t2l][1] - deduct)

                if t1[t1r][1] - deduct == 0:
                    t1r -= 1
                else:
                    t1[t1r] = (t1[t1r][0], t1[t1r][1] - deduct)

        return cost
