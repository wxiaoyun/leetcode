# https://leetcode.com/problems/count-sub-islands/

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R = len(grid1)
        C = len(grid1[0])
        islands = set()
        island_count = 0

        def flood(i: int, j: int, val: int) -> None:
          if min(i, j) < 0 or i >= R or j >= C:
            return None
          
          if grid2[i][j] != 1:
            return None
          
          grid2[i][j] = val
          for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            flood(r, c, val)
        
        # Find islands first
        for r in range(R):
          for c in range(C):
            if grid2[r][c] == 1:
              island_count += 1
              islands.add(island_count)
              flood(r, c, -island_count)

        # Check if these islands are sub islands
        for r in range(R):
          for c in range(C):
            if grid1[r][c] == 0 and grid2[r][c] < 0:
              island = abs(grid2[r][c])
              if island in islands:
                islands.remove(island)
        
        return len(islands)