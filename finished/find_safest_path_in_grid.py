# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safety_value = [[float('inf') for _ in row] for row in grid]

        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                queue.append((r, c, 0))
        
        visited = [[False for _ in row] for row in grid]

        while len(queue) > 0:
            r, c, s = queue.popleft()
            if min(r, c) < 0 or r >= n or c >= n or visited[r][c]:
                continue


            safety_value[r][c] = min(safety_value[r][c], s)
            s+=1
            visited[r][c] = True

            queue.extend([
                (r+1, c, s),
                (r-1, c, s),
                (r, c+1, s),
                (r, c-1, s)
            ])

        
        direction = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def dikjstra(r=0, c=0):
            pq = [(-safety_value[r][c], r, c)]
            visited = [[False for _ in row] for row in grid]

            while len(pq) > 0:
                s, r, c = heapq.heappop(pq)
                s = -s

                if r == n-1 and c == n-1:
                    return s
                
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc

                    if min(nr, nc) < 0 or nr >= n or nc >= n or visited[nr][nc]:
                        continue
                    visited[nr][nc] = True

                    ns = safety_value[nr][nc]
                    heapq.heappush(pq, (-min(s, ns), nr, nc))
        
        return dikjstra()
