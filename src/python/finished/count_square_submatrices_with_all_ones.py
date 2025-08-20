from copy import copy
from typing import List

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def count(matrix: List[List[int]], dim: List[List[int]], i: int, j: int) -> int:
            R = len(matrix)
            C = len(matrix[0])
            if i >= R or j >= C or matrix[i][j] == 0:
                return 0

            if not dim[i][j] < 0:
                return dim[i][j]

            largest = 1 << 31
            for di in range(2):
                for dj in range(2):
                    if di == 0 and di == dj:
                        continue
                    largest = min(largest, count(matrix, dim, i + di, j + dj))

            dim[i][j] = largest + 1
            return largest + 1

        R = len(matrix)
        C = len(matrix[0])
        dim = [[-1] * C for _ in range(R)]
        return sum(sum(count(matrix, dim, i, j) for j in range(C)) for i in range(R))


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        max_square = copy.deepcopy(matrix)

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c]:
                    max_square[r][c] = (
                        min(
                            max_square[r - 1][c - 1],
                            max_square[r - 1][c],
                            max_square[r][c - 1],
                        )
                        + 1
                    )

        return sum([sum(row) for row in max_square])


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])

        dp = copy.deepcopy(matrix)
        answer = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] and i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                answer += dp[i][j]
        return answer
