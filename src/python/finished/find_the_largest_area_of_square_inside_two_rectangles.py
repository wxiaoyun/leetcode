from typing import List

# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        def largest_square_area(bottomLeft, topRight, a: int, b: int) -> int:
            l = max(bottomLeft[a][0], bottomLeft[b][0])
            r = min(topRight[a][0], topRight[b][0])
            lo = max(bottomLeft[a][1], bottomLeft[b][1])
            tp = min(topRight[a][1], topRight[b][1])

            side = max(0, min(r - l, tp - lo))
            return side * side

        n = len(bottomLeft)
        assert n == len(topRight)

        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_area = max(
                    max_area, largest_square_area(bottomLeft, topRight, i, j)
                )
        return max_area
