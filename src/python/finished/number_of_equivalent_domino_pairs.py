from typing import List
from collections import Counter

# https://leetcode.com/problems/number-of-equivalent-domino-pairs


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter()

        total = 0
        for a, b in dominoes:
            key = (1 << a) | (1 << b)
            current_count = cnt[key]
            total += current_count
            cnt[key] = current_count + 1

        return total
