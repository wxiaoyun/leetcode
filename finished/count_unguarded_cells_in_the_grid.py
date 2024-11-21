from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
      g, w = 'G', 'W'
      grid = [[None] * n for i in range(m)]
      for rg, cg in guards:
        grid[rg][cg] = g
      for rw, cw in walls:
        grid[rw][cw] = w

      row_prefix = [[w] * n for i in range(m)]
      row_suffix = [[w] * n for i in range(m)]
      col_prefix = [[w] * n for i in range(m)]
      col_suffix = [[w] * n for i in range(m)]
      
      # row_prefix
      for r in range(m):
        for c in range(1, n):
          if grid[r][c-1]:
            row_prefix[r][c] = grid[r][c-1]
          else:
            row_prefix[r][c] = row_prefix[r][c-1]
      
      # row_suffix
      for r in range(m):
        for c in reversed(range(0, n-1)):
          if grid[r][c+1]:
            row_suffix[r][c] = grid[r][c+1]
          else:
            row_suffix[r][c] = row_suffix[r][c+1]

      # col_prefix
      for c in range(n):
        for r in range(1, m):
          if grid[r-1][c]:
            col_prefix[r][c] = grid[r-1][c]
          else:
            col_prefix[r][c] = col_prefix[r-1][c]
      
      # col_suffix
      for c in range(n):
        for r in reversed(range(0, m-1)):
          if grid[r+1][c]:
            col_suffix[r][c] = grid[r+1][c]
          else:
            col_suffix[r][c] = col_suffix[r+1][c]
      
      # for mat in [grid, row_prefix, row_suffix, col_prefix, col_suffix]:
      #   for row in mat:
      #     print(row)
      #   print()

      count = 0
      for r in range(m):
        for c in range(n):
          if grid[r][c]:
            continue
          
          if (
            row_prefix[r][c] == w and
            row_suffix[r][c] == w and
            col_prefix[r][c] == w and
            col_suffix[r][c] == w
          ):
           count += 1
      
      return count


    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[None] * n for i in range(m)]

        g, w = 'G', 'W'
        for rg, cg in guards:
          grid[rg][cg] = g
        for rw, cw in walls:
          grid[rw][cw] = w
        
        for r in range(m):
          for c in range(n):
            if grid[r][c] != g:
              continue
            
            for i in range(r-1, -1, -1):
              if grid[i][c] == g or grid[i][c] == w:
                break
              
              grid[i][c] = 'S'

            for i in range(r+1, m):
              if grid[i][c] == g or grid[i][c] == w:
                break
              
              grid[i][c] = 'S'

            for j in range(c-1, -1, -1):
              if grid[r][j] == g or grid[r][j] == w:
                break
              
              grid[r][j] = 'S'

            for j in range(c+1, n):
              if grid[r][j] == g or grid[r][j] == w:
                break
              
              grid[r][j] = 'S'
          
        count = 0
        for i in range(m):
          for j in range(n):
            if grid[i][j] == None:
              count += 1
        return count