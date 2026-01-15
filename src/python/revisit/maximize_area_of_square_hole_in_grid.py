from collections import defaultdict
from typing import List

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # observation:
        # to create a square hole, we must remove bars in a diagonal direction
        # e.g. (horizontal, vertical): remove (1, 1), (2, 2), (3, 3) to create a 4 by 4 hole

        # algo: find the longest continuous diagonal streak

        nrow = n + 2
        ncol = m + 2

        diags = defaultdict(list)
        for r in hBars:
            rr = r - 1
            for c in vBars:
                cc = c - 1
                diag = rr + (ncol - 1 - cc)
                diags[diag].append(rr)

        max_streak = 0
        for diag in diags.values():
            diag = sorted(diag)

            streak = 1
            max_streak = max(max_streak, streak)

            for i in range(1, len(diag)):
                if diag[i - 1] == diag[i] - 1:
                    streak += 1
                else:
                    streak = 1
                max_streak = max(max_streak, streak)

        return (max_streak + 1) ** 2
