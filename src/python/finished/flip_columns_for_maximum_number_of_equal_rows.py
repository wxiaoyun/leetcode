from collections import Counter
from typing import List

# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        C = len(matrix[0])
        half = 1 << (C - 1) # Get "10000000" with (C-1) zeros
        ones = (1 << C) - 1 # Get "11111111" with C ones

        vals = []
        for row in matrix:
          tmp = 0
          for n in row:
            tmp *= 2
            tmp += n
          if tmp < half:
            tmp = tmp ^ ones
          vals.append(tmp)

        cnt = Counter(vals)
        return max(cnt.values())