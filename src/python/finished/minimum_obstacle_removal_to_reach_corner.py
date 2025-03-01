from collections import deque
from typing import List

# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dest = (N - 1, M - 1)

        nextq = deque()
        q = deque([(0, 0)])
        visited = set()
        dist = 0
        while q or nextq:
          if not q:
            dist += 1
            q = nextq
            nextq = deque() # reset 
        
          node = q.popleft()
          if node in visited:
            continue
          visited.add(node)

          if node == dest:
            return dist

          i, j = node
          for ii, jj in [
            (i+1, j),
            (i-1, j),
            (i, j+1),
            (i, j-1),
          ]:
            if min(ii, jj) < 0 or ii >= N or jj >= M:
              continue
            if grid[ii][jj] == 1:
              nextq.append((ii, jj))
            else:
              q.append((ii, jj))

        return -1

    # def minimumObstacles(self, grid: List[List[int]]) -> int:
    #     N = len(grid)
    #     M = len(grid[0])

    #     def get_adj_nodes(i: int, j: int) -> List[Tuple[int, int, int]]:
    #       edges = []
    #       for ii, jj in [
    #         [i+1, j],
    #         [i-1, j],
    #         [i, j+1],
    #         [i, j-1],
    #       ]:
    #         if min(ii, jj) < 0 or ii >= N or jj >= M:
    #           continue
    #         edges.append((grid[ii][jj], ii, jj))
    #       return edges

    #     pq = [(0, 0, 0)]
    #     visited = set()
    #     dest = (N-1, M-1)
    #     while pq:
    #       c, i, j = heapq.heappop(pq)
    #       node = (i, j)

    #       if node in visited:
    #         continue
    #       visited.add(node)

    #       if node == dest:
    #         return c
          
    #       for w, ii, jj in get_adj_nodes(i, j):
    #         heapq.heappush(pq, (c+w, ii, jj))
    #     return -1