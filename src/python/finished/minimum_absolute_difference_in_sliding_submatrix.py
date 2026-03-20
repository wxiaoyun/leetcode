from typing import List

# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for top in range(m - k + 1):
            for left in range(n - k + 1):
                values = set()
                for r in range(top, top + k):
                    for c in range(left, left + k):
                        values.add(grid[r][c])
                if len(values) == 1:
                    continue

                value_ls = sorted(list(values))
                ans[top][left] = min(
                    value_ls[i] - value_ls[i - 1] for i in range(1, len(value_ls))
                )

        return ans
