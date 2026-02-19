# https://leetcode.com/problems/count-binary-substrings/


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pcnt, ccnt = 0, 0
        cur = ""

        n_sub = 0
        for ch in s:
            if ch != cur:
                pcnt = ccnt
                ccnt = 0
                cur = ch

            ccnt += 1
            if ccnt <= pcnt:
                n_sub += 1

        return n_sub
