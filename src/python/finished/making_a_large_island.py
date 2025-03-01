from collections import deque
from typing import List

# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        comp = -1

        def flood(r: int, c: int, comp: int) -> int:
            q = deque([(r, c)])
            size = 0

            while q:
                r, c = q.popleft()

                if grid[r][c] <= 0:
                    continue
                grid[r][c] = comp
                size += 1

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= N or cc >= N:
                        continue
                    q.append((rr, cc))
            
            return size
        
        comp_size = {0: 0}
        for r in range(N):
            for c in range(N):
                if not grid[r][c] > 0:
                    continue
                
                size = flood(r, c, comp)
                comp_size[comp] = size
                comp -= 1
        
        # print(grid)
        # print(comp_size)
        best = 0
        for r in range(N):
            for c in range(N):
                total = 0 if grid[r][c] < 0 else 1
                dup = set()
                for rr, cc in [
                    (r, c),
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= N or cc >= N:
                        continue
                    comp = grid[rr][cc]
                    if comp in dup:
                        continue
                    dup.add(comp)
                    total += comp_size[comp]
                
                best = max(best, total)

        return best





