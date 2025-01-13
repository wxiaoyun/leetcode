from collections import Counter

# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)

        l = 0
        for ch, freq in cnt.items():
            if freq >= 3:
                l += 2 - (freq % 2)
            else:
                l += freq

        return l