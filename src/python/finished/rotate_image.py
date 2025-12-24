import math
from typing import List

# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # (0, 0) -> (0, n - 1)
        # (0, 1) -> (1, n - 1)
        # ...
        # (0, n - 2) -> (n - 2, n - 1)
        # (0, n - 1) -> (n - 1, n - 1)
        # ...
        # (n - 1, n - 1) -> (n - 1, 0)

        # Pattern:
        # (l, r) -> (r, n - l - 1)

        n = len(matrix)
        m = len(matrix[0])

        for i in range(math.floor(n / 2)):
            for j in range(math.ceil(m / 2)):
                cur_i, cur_j = i, j
                cur = matrix[i][j]
                for _ in range(4):
                    next_i, next_j = cur_j, n - cur_i - 1

                    nxt = matrix[next_i][next_j]
                    matrix[next_i][next_j] = cur
                    cur = nxt

                    cur_i, cur_j = next_i, next_j
