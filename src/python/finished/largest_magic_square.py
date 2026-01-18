from typing import List

# https://leetcode.com/problems/largest-magic-square/


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        k = min(n, m)
        while k > 0:
            # try find a magic square of width k
            for i in range(n - k + 1):
                for j in range(m - k + 1):
                    target = sum(v for v in grid[i][j : j + k])

                    cols_eq = all(
                        sum(grid[r][c] for c in range(j, j + k)) == target
                        for r in range(i, i + k)
                    )
                    rows_eq = all(
                        sum(grid[r][c] for r in range(i, i + k)) == target
                        for c in range(j, j + k)
                    )
                    diag_eq = (
                        target
                        == sum(grid[i + d][j + d] for d in range(k))
                        == sum(grid[i + d][j + k - d - 1] for d in range(k))
                    )

                    if cols_eq and rows_eq and diag_eq:
                        return k

            k -= 1

        return 0
