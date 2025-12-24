from typing import List

# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        MARKER = 1 << 31

        for i in range(n):
            found_zero = False
            for j in range(m):
                if matrix[i][j] == 0:
                    found_zero = True
                    break

            if not found_zero:
                continue

            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = MARKER

        for j in range(m):
            found_zero = False
            for i in range(n):
                if matrix[i][j] == 0:
                    found_zero = True
                    break

            if not found_zero:
                continue

            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = MARKER

        for i in range(n):
            for j in range(m):
                if matrix[i][j] != MARKER:
                    continue

                matrix[i][j] = 0
