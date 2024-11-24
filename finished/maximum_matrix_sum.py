from typing import List

# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        lt_cnt = 0
        total, smallest = 0, float('inf')
        for row in matrix:
          for n in row:
            if n < 0:
              lt_cnt += 1
            total += abs(n)
            smallest = min(smallest, abs(n))
        
        if lt_cnt % 2 == 0:
          return total
        return total - 2 * smallest