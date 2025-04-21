from typing import List

# https://leetcode.com/problems/count-the-hidden-sequences


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mn, mx = 0, 0
        prev = 0
        for i in range(len(differences)):
            n = prev + differences[i]
            mn = min(mn, n)
            mx = max(mx, n)
            prev = n
        return max(0, (upper - lower) - (mx - mn) + 1)
