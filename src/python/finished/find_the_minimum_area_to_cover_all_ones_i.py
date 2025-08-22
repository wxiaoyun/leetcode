# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        lb, rb = C, -1
        tb, bb = R, -1

        for r in range(R):
            for c in range(C):
                cell = grid[r][c]
                if not cell:
                    continue
                lb = min(lb, c)
                rb = max(rb, c)
                tb = min(tb, r)
                bb = max(bb, r)

        return max(0, (rb - lb + 1) * (bb - tb + 1))
