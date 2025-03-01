# https://leetcode.com/problems/regions-cut-by-slashes/


from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
      R = len(grid)
      C = len(grid[0])

      wall = -1
      directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
      flood_grid = [[0] * (3*C)  for _ in range(3*R)]

      for r in range(R):
        for c in range(C):
          if grid[r][c] == "/":
            flood_grid[3*r][3*c+2] = wall
            flood_grid[3*r+1][3*c+1] = wall
            flood_grid[3*r+2][3*c] = wall
          elif grid[r][c] == "\\":
            flood_grid[3*r][3*c] = wall
            flood_grid[3*r+1][3*c+1] = wall
            flood_grid[3*r+2][3*c+2] = wall
        
      def flood(r: int, c: int) -> None:
        if min(r, c) < 0 or r >= len(flood_grid) or c >= len(flood_grid[0]):
          return
        if flood_grid[r][c]:
          return

        flood_grid[r][c] = 1
        for dx, dy in directions:
          flood(r+dx, c+dy)
      
      regions_count = 0
      for r in range(3*R):
        for c in range(3*C):
          if not flood_grid[r][c]:
            regions_count += 1
            flood(r, c)
      
      return regions_count