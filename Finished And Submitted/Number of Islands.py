from typing import List

#  https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        marked = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islandCount = 0
          
        def flood(r: int, c: int) -> None:
          marked[r][c] = True
          if r > 0 and grid[r - 1][c] == "1" and not marked[r - 1][c]:
             flood(r - 1, c)
          if r < len(grid) - 1 and grid[r + 1][c] == "1" and not marked[r + 1][c]:
              flood(r + 1, c)
          if c > 0 and grid[r][c - 1] == "1" and not marked[r][c - 1]:
              flood(r, c - 1)
          if c < len(grid[0]) - 1 and grid[r][c + 1] == "1" and not marked[r][c + 1]:
              flood(r, c + 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not marked[r][c]:
                    flood(r, c)
                    islandCount += 1
        return islandCount