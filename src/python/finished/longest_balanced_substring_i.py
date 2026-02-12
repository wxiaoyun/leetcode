from collections import Counter

# https://leetcode.com/problems/longest-balanced-substring-i


class Solution:
    def longestBalanced(self, s: str) -> int:
        best = 0

        for l in range(len(s)):
            cnt = Counter()
            for r in range(l, len(s)):
                rch = s[r]
                cnt[rch] += 1
                if all(c == cnt[rch] for c in cnt.values()):
                    best = max(best, r - l + 1)
        return best
