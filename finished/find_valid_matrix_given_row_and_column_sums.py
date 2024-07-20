from typing import List, Optional


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
      # def helper(matrix: List[List[int]], rowSum: List[int], colSum: List[int], r: int, c: int) -> Optional[List[List[int]]]:
      #   if min(r, c) < 0 or r >= len(rowSum) or c >= len(colSum):
      #       if sum(rowSum) + sum(colSum) == 0:
      #         return matrix
      #       else:
      #         return None

      #   oRowSum = rowSum[r]
      #   oColSum = colSum[c]
      #   # this ensures that rowSum and colSum is always non-negative
      #   to = min(oRowSum, oColSum)

      #   j = r*len(colSum)+c+1
      #   nr = j // len(colSum)
      #   nc = j % len(colSum)

      #   for i in reversed(range(to+1)): # inclusive of to
      #     matrix[r][c] = i
      #     rowSum[r] = oRowSum - i
      #     colSum[c] = oColSum - i
          
      #     result = helper(matrix, rowSum, colSum, nr, nc)
      #     if result:
      #       return result
        
      #   rowSum[r] = oRowSum
      #   colSum[c] = oColSum
      #   return None
      
      # return helper([[0 for _ in colSum] for _ in rowSum], rowSum, colSum, 0, 0)

      mat = [[0 for _ in colSum] for _ in rowSum]
      for i in range(len(rowSum)):
        for j in range(len(colSum)):
          mat[i][j] = min(rowSum[i], colSum[j])
          rowSum[i] -= mat[i][j]
          colSum[j] -= mat[i][j]
      return mat