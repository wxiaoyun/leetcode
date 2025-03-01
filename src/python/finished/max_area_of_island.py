from collections import deque
from typing import List

# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()

        def flood_area(i: int, j: int) -> int:
            q = deque([(i, j)])
            area = 0

            while q:
                cell = q.popleft()

                if cell in visited:
                    continue
                visited.add(cell)
                
                r, c = cell
                if grid[r][c] == 0:
                    continue
                
                area += 1

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue
                    
                    q.append((rr, cc))

            return area
        
        area = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = max(area, flood_area(r, c))
        
        return area