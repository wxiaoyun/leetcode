from collections import Counter

# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = sorted(Counter(word).values(), reverse=True)

        npress = 0
        for i in range(len(cnt)):
            f = cnt[i]
            npress += (1 + i // 8) * f
        return npress
