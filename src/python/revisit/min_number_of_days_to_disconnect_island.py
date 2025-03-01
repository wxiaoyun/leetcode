# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

from copy import copy
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def count_islands() -> int:
          count = 0
          cp = copy.deepcopy(grid)

          def flood(i: int, j: int) -> None:
            if min(i, j) < 0 or i >= R or j >= C:
              return
            if cp[i][j] != 1:
              return
            
            cp[i][j] = 2
            for x, y in [
              (i+1, j),
              (i-1, j),
              (i, j+1),
              (i, j-1),
            ]:
              flood(x, y)
          
          for i in range(R):
            for j in range(C):
              if cp[i][j] == 1:
                count += 1
                flood(i, j)

          return count
        
        count = count_islands()
        if count != 1:
          return 0
        
        for i in range(R):
          for j in range(C):
            if grid[i][j] == 0:
              continue
            grid[i][j] = 0
            count = count_islands()
            if count != 1:
              return 1
            grid[i][j] = 1

        return 2


        