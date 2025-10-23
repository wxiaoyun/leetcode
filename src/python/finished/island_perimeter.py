# https://leetcode.com/problems/island-perimeter

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        p = 0
        for r in range(R + 1):
            for c in range(C):
                prev = grid[r - 1][c] if r > 0 else 0
                this = grid[r][c] if r < R else 0
                if prev != this:
                    p += 1

        for c in range(C + 1):
            for r in range(R):
                prev = grid[r][c - 1] if c > 0 else 0
                this = grid[r][c] if c < C else 0
                if prev != this:
                    p += 1

        return p
