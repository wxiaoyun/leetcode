from typing import List

# https://leetcode.com/problems/flip-square-submatrix-vertically/


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        def swap_row(grid: List[List[int]], r1: int, r2: int, c: int, k: int) -> None:
            for j in range(c, c + k):
                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]

        r1, r2 = x, x + k - 1
        while r1 < r2:
            swap_row(grid, r1, r2, y, k)
            r1 += 1
            r2 -= 1
        return grid
