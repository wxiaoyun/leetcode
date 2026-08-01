from collections import Counter

# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)

        npush = 0
        step = 1
        while l > 0:
            npush += step * min(8, l)
            l -= 8
            step += 1
        return npush
