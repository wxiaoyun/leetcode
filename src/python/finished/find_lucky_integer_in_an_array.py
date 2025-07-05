from collections import Counter
from typing import List

# https://leetcode.com/problems/find-lucky-integer-in-an-array


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        best = -1
        for k, v in cnt.items():
            if k == v:
                best = max(best, k)
        return best
