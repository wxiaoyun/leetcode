from collections import Counter

# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        max_odd, min_even = 0, float("inf")
        for f in c.values():
            if f % 2 == 0:
                min_even = min(min_even, f)
            else:
                max_odd = max(max_odd, f)

        return max_odd - min_even
