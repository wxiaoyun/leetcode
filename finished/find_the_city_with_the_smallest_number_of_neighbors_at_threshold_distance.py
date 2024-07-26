# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#       # type Edge = Tuple[int, int]
#       adj_list: Dict[int, List[Edge]] = {}

#       for i in range(n):
#         adj_list[i] = []
#       for fr, to, w in edges:
#         adj_list[fr].append((to, w))
#         adj_list[to].append((fr, w))
      
#       def dikjstra(src: int) -> int:
#         visited = set()
#         pq = [(0, src)]

#         while pq:
#           dist, n = heapq.heappop(pq)

#           if dist > distanceThreshold:
#             break
          
#           if n in visited:
#             continue
          
#           visited.add(n)
#           for ngbr, w in adj_list[n]:
#             heapq.heappush(pq, (dist+w, ngbr))
        
#         if src in visited:
#           visited.remove(src)
#         return len(visited)
      
#       def cmptr(a, b):
#         if a[0] != b[0]:
#           return a[0] - b[0]
#         return -(a[1] - b[1])

#       return min(
#         [(dikjstra(n), n) for n in adj_list.keys()],
#         key=functools.cmp_to_key(cmptr)
#       )[1]

import functools
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
      dist = [[float('inf')] * n for _ in range(n)]

      for i in range(n):
        dist[i][i] = 0
      
      for fr, to, w in edges:
        dist[fr][to] = w
        dist[to][fr] = w
      
      for k in range(n):
        for i in range(n):
          for j in range(n):
            dist[i][j] = min(
              dist[i][j],
              dist[i][k] + dist[k][j]
            )
      
      neighbours = {node: 0 for node in range(n)}
      for i in range(n):
        for j in range(n):
          if i != j and dist[i][j] <= distanceThreshold:
            neighbours[i] += 1

      def cmptr(a, b):
        if a[0] != b[0]:
          return a[0] - b[0]
        return -(a[1] - b[1])

      return min(
        [(cnt, n) for n, cnt in neighbours.items()],
        key=functools.cmp_to_key(cmptr)
      )[1]