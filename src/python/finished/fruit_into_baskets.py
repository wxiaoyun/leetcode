# https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        freq_cnt = [[fruits[0], 1]]
        for i in range(1, N):
            if fruits[i] == fruits[i - 1]:
                freq_cnt[-1][1] += 1
                continue

            freq_cnt.append([fruits[i], 1])

        types = defaultdict(int)
        best, cur = 0, 0
        i = 0
        for f, c in freq_cnt:
            types[f] += c
            cur += c

            while len(types) > 2:
                ff, cc = freq_cnt[i]
                i += 1
                cur -= cc
                types[ff] -= cc
                if types[ff] == 0:
                    del types[ff]
            best = max(best, cur)

        return best
