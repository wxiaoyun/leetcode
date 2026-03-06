# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segs = 0
        for i in range(1, len(s) + 1):
            prev = s[i - 1]
            cur = s[i] if i < len(s) else "0"
            if prev == cur:
                continue
            if cur == "0":
                segs += 1
        return segs == 1
