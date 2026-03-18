# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/


from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix_area = [[0] * n for _ in range(m)]

        n_mat = 0
        for i in range(m):
            for j in range(n):
                left_area = prefix_area[i][j - 1] if j > 0 else 0
                top_area = prefix_area[i - 1][j] if i > 0 else 0
                top_left_area = prefix_area[i - 1][j - 1] if i > 0 and j > 0 else 0
                prefix_area[i][j] = grid[i][j] + left_area + top_area - top_left_area
                if prefix_area[i][j] <= k:
                    n_mat += 1

        return n_mat
