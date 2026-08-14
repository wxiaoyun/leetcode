from collections import Counter

# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        best = 0
        cnt = Counter()
        l = 0
        for r in range(len(s)):
            rch = s[r]
            cnt[rch] += 1
            while cnt[rch] > 2:
                cnt[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)

        return best
