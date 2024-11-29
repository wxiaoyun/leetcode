import heapq
from typing import List

# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dest = (R-1, C-1)

        have_prev = False
        if (C > 1 and grid[0][1] <= 1) or (R > 1 and grid[1][0] <= 1):
          have_prev = True

        pq = [(0, 0, 0, have_prev)] 
        visited = set()
        while pq:
          t, r, c, have_prev = heapq.heappop(pq)
          node = (r, c)

          if node in visited:
            continue
          visited.add(node)

          if node == dest:
            return t
          
          for rr, cc in [
            (r + 1, c),
            (r - 1, c),
            (r, c + 1),
            (r, c - 1),
          ]:
            if min(rr, cc) < 0 or rr >= R or cc >= C:
              continue
            if t+1 >= grid[rr][cc]:
              heapq.heappush(pq, (t+1, rr, cc, True))
            elif have_prev:
              time_diff = (grid[rr][cc] - (t+1)) % 2
              heapq.heappush(pq, (grid[rr][cc] + time_diff, rr, cc, True))

        return -1