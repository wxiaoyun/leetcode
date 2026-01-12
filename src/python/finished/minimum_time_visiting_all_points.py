from typing import List

# https://leetcode.com/problems/minimum-time-visiting-all-points


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0

        for i in range(1, len(points)):
            px, py = points[i - 1]
            x, y = points[i]

            dx, dy = abs(px - x), abs(py - y)
            diag = min(dx, dy)

            t += diag + (dx - diag) + (dy - diag)

        return t
