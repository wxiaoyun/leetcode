# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = -1
        diag_sq = -1
        for l, w in dimensions:
            local_diag_sq = l * l + w * w
            if local_diag_sq > diag_sq:
                area = l * w
                diag_sq = local_diag_sq
            elif local_diag_sq == diag_sq:
                area = max(area, l * w)
        return area
