from typing import List

# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # moves[i][j] = 1 + max(moves[i - 1][j - 1], moves[i][j - 1], moves[i + 1][j - 1])
        r = len(grid)
        c = len(grid[0])

        best = 0
        moves = [1] * r
        for j in range(1, c):
          tmp = [0] * r

          for i in range(r):
            cur = grid[i][j]
            if i > 0 and moves[i-1] > 0 and cur > grid[i-1][j-1]:
              tmp[i] = max(tmp[i], moves[i-1] + 1)
            if moves[i] > 0 and cur > grid[i][j-1]:
              tmp[i] = max(tmp[i], moves[i] + 1)
            if i < r-1 and moves[i+1] > 0 and cur > grid[i+1][j-1]:
              tmp[i] = max(tmp[i], moves[i+1] + 1)
            best = max(best, tmp[i]-1)
          moves = tmp
        
        return best