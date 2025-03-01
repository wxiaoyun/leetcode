from copy import copy
from typing import List

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        max_square = copy.deepcopy(matrix)

        for r in range(1, len(matrix)):
          for c in range(1, len(matrix[0])):
            if matrix[r][c]:
              max_square[r][c] = min(
                max_square[r-1][c-1],
                max_square[r-1][c],
                max_square[r][c-1],
              ) + 1

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
              dp[i][j] = min(
                dp[i - 1][j - 1],
                dp[i - 1][j],
                dp[i][j - 1]
              ) + 1
            answer += dp[i][j]
        return answer

# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         r = len(matrix)
#         c = len(matrix[0])

#         def is_square(l: int, i: int, j: int) -> bool:
#           for rr in range(i, i+l):
#             for cc in range(j, j+l):
#               if not matrix[rr][cc]:
#                 return False
#           return True
        
#         count = 0
#         for l in range(1, min(r, c)+1):
#           for i in range(r-l+1):
#             for j in range(c-l+1):
#               if is_square(l, i, j):
#                 count += 1
#         return count