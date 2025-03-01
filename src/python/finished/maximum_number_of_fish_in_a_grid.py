from collections import deque
from typing import List

# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def flood(i: int, j: int) -> int:
            q = deque([(i, j)])

            fish = 0
            while q:
                i, j = q.popleft()
                
                w = grid[i][j]
                if w < 0:
                    continue
                grid[i][j] = -1

                if w == 0:
                    continue
                fish += w
                
                for rr, cc in [
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue
                    q.append((rr, cc))
            
            return fish

        best = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    best = max(best, flood(r, c))
        return best