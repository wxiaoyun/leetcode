from typing import List

# https://leetcode.com/problems/construct-product-matrix


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        ans = [[-1] * n for _ in range(m)]

        suffix_prod = 1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                ans[r][c] = suffix_prod
                suffix_prod = (suffix_prod * grid[r][c]) % MOD

        prefix_prod = 1
        for r in range(m):
            for c in range(n):
                ans[r][c] = (ans[r][c] * prefix_prod) % MOD
                prefix_prod = (prefix_prod * grid[r][c]) % MOD

        return ans
