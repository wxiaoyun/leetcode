from typing import List
from collections import deque

# https://leetcode.com/problems/longest-subsequence-repeated-k-times


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def check(s: str, k: int, seq: List[str]) -> bool:
            seqlen = len(seq)
            i = 0
            for ch in s:
                if ch == seq[i % seqlen]:
                    i += 1

                    if i >= (k * seqlen):
                        return True

            return False

        cur = deque([[]])
        while cur:
            nxt = deque()
            level = len(cur)
            for i in range(level):
                seq = cur[i]

                for i in range(26):
                    ch = chr(ord("a") + i)
                    seqq = seq[:]
                    seqq.append(ch)

                    if check(s, k, seqq):
                        nxt.append(seqq)

            if len(nxt) == 0:
                return "".join(cur[-1])

            cur = nxt

        return ""
