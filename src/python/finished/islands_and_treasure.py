from collections import deque
from typing import List

# https://neetcode.io/problems/islands-and-treasure

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, d = q.popleft()

            if grid[r][c] == -1:
                continue
            if d != 0 and d >= grid[r][c]:
                continue
            grid[r][c] = d

            for dr, dc in [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
            ]:
                rr, cc = r + dr, c + dc
                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                q.append((rr, cc, d + 1))

        return None