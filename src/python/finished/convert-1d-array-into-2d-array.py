# https://leetcode.com/problems/convert-1d-array-into-2d-array/

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != m*n:
          return res
       
        for i in range(m):
          row = []
          res.append(row)
          for j in range(n):
            row.append(original[i*n+j])
        return res