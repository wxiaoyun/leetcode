from typing import List

# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        rows = [[] for _ in range(R)]
        cols = [[] for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    rows[r].append(c)
                    cols[c].append(r)

        com = set()
        for r, row in enumerate(rows):
            if len(row) < 2:
                continue
            
            for c in row:
                com.add((r, c))
        
        for c, col in enumerate(cols):
            if len(col) < 2:
                continue
            
            for r in col:
                com.add((r, c))
        
        return len(com)
