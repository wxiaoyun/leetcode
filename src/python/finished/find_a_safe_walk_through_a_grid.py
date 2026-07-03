from collections import deque
from typing import List

# https://leetcode.com/problems/find-a-safe-walk-through-a-grid


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        q = deque([(0, 0)])
        if grid[0][0] > 0:
            health -= 1
        visited = set()
        qnext = deque()
        while health > 0 and (q or qnext):
            if q:
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                if (r, c) == (R - 1, C - 1):
                    return True

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue
                    if (rr, cc) in visited:
                        continue

                    if grid[rr][cc] == 0:
                        q.append((rr, cc))
                    else:
                        qnext.append((rr, cc))
            else:
                health -= 1
                q, qnext = qnext, q
                qnext.clear()

        return False
