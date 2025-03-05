# https://leetcode.com/problems/count-total-number-of-colored-cells


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 4 // 2


class Solution:
    def coloredCells(self, n: int) -> int:
        # 1: 1
        # 2: 1 + 1 * 4
        # 3: (1+1*4) + 2 * 4
        # n: c(n-1) + (n-1) * 4

        c = 1
        for t in range(1, n):
            c = c + t * 4
        return c
