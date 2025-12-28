from typing import List

# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        total = 0

        for j in range(m):
            if grid[0][j] < 0:
                total += n
                continue

            row = n
            l, r = 0, n
            while l < r:
                mid = l + (r - l) // 2
                if grid[mid][j] >= 0:
                    # this entire row is non-neg
                    l = mid + 1
                else:
                    row = mid
                    r = mid

            total += n - row

        return total
