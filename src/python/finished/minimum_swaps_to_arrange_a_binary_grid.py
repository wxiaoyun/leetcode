from typing import List

# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = []
        for row in grid:
            one_idx = -1
            for i in reversed(range(n)):
                if row[i] == 1:
                    one_idx = i
                    break
            rows.append(one_idx)

        swaps = 0
        for i in range(n):
            target = -1
            for j in range(i, n):
                if rows[j] <= i:
                    target = j
                    break

            if target < 0:
                return -1

            for k in reversed(range(i, j)):
                rows[k], rows[k + 1] = rows[k + 1], rows[k]
            swaps += j - i

        return swaps
