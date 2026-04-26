from typing import List

# https://leetcode.com/problems/detect-cycles-in-2d-grid/


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = set()

        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue

                val = grid[i][j]
                local_visited = set()
                stk = [(i, j, -1, -1)]
                while stk:
                    ii, jj, pi, pj = stk.pop()
                    if (ii, jj) in local_visited:
                        return True

                    local_visited.add((ii, jj))

                    for r, c in [
                        (ii - 1, jj),
                        (ii + 1, jj),
                        (ii, jj - 1),
                        (ii, jj + 1),
                    ]:
                        if (r, c) == (pi, pj):
                            continue
                        if min(r, c) < 0 or r >= n or c >= m:
                            continue
                        if grid[r][c] != val:
                            continue
                        stk.append((r, c, ii, jj))

                visited.update(local_visited)

        return False
