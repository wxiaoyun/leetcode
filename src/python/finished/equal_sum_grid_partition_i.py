from typing import List

# https://leetcode.com/problems/equal-sum-grid-partition-i/


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        hori_prefix_sum = [0]
        for r in range(m):
            hori_prefix_sum.append(hori_prefix_sum[-1] + sum(grid[r]))

        for r in range(m):
            if hori_prefix_sum[r] * 2 == hori_prefix_sum[-1]:
                return True

        vert_prefix_sum = [0]
        for c in range(n):
            vert_prefix_sum.append(
                vert_prefix_sum[-1] + sum(grid[r][c] for r in range(m))
            )

        for c in range(n):
            if vert_prefix_sum[c] * 2 == vert_prefix_sum[-1]:
                return True

        return False
