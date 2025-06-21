from collections import Counter

# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)

        best = sum(cnt.values())
        for ch, fq in cnt.items():
            cur = 0
            for f in cnt.values():
                if f < fq:
                    cur += f
                elif f > fq + k:
                    cur += f - (fq + k)
            best = min(best, cur)
        return best
