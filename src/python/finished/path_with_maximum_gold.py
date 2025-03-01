# https://leetcode.com/problems/path-with-maximum-gold/

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]

        def dfs(i: int, j: int, cur: int) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return cur
            if visited[i][j]:
                return cur
            if grid[i][j] == 0:
                return cur
            
            visited[i][j] = True
            cur += grid[i][j]

            best = max(
                dfs(i+1, j, cur),
                dfs(i-1, j, cur),
                dfs(i, j+1, cur),
                dfs(i, j-1, cur)
            )            

            visited[i][j] = False

            return best
        
        best = -float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                best = max(best, dfs(i, j, 0))
        
        return best
