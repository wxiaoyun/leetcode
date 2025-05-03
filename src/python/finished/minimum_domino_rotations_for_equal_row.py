from typing import List

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        cur = (1 << 8) - 1
        for i in range(N):
            local = (1 << tops[i]) | (1 << bottoms[i])
            cur = cur & local

            if cur == 0:
                return -1

        bcur = list(bin(cur)[2:])
        bcur.reverse()

        best = float("inf")
        for digit, bit in enumerate(bcur):
            if bit != "1":
                continue

            count_top, count_bottom = 0, 0
            for i in range(N):
                if tops[i] != digit:
                    count_top += 1
                if bottoms[i] != digit:
                    count_bottom += 1

            best = min(best, count_top, count_bottom)

        return best
