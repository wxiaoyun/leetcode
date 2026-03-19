from typing import List

# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        prefix_x = [[0] * n for _ in range(m)]
        prefix_y = [[0] * n for _ in range(m)]

        ans = 0
        for r in range(m):
            for c in range(n):
                x_left = prefix_x[r][c - 1] if c > 0 else 0
                y_left = prefix_y[r][c - 1] if c > 0 else 0

                x_top = prefix_x[r - 1][c] if r > 0 else 0
                y_top = prefix_y[r - 1][c] if r > 0 else 0

                x_top_left = prefix_x[r - 1][c - 1] if r > 0 and c > 0 else 0
                y_top_left = prefix_y[r - 1][c - 1] if r > 0 and c > 0 else 0

                x_cnt = x_left + x_top - x_top_left + (1 if grid[r][c] == "X" else 0)
                y_cnt = y_left + y_top - y_top_left + (1 if grid[r][c] == "Y" else 0)

                prefix_x[r][c] = x_cnt
                prefix_y[r][c] = y_cnt

                if x_cnt > 0 and x_cnt == y_cnt:
                    ans += 1

        return ans
