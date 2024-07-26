# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance

import functools
import heapq
from typing import Dict, List, Tuple


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
      type Edge = Tuple[int, int]
      adj_list: Dict[int, List[Edge]] = {}

      for i in range(n):
        adj_list[i] = []
      for fr, to, w in edges:
        adj_list[fr].append((to, w))
        adj_list[to].append((fr, w))
      
      def dikjstra(src: int) -> int:
        visited = set()
        pq = [(0, src)]

        while pq:
          dist, n = heapq.heappop(pq)

          if dist > distanceThreshold:
            break
          
          if n in visited:
            continue
          
          visited.add(n)
          for ngbr, w in adj_list[n]:
            heapq.heappush(pq, (dist+w, ngbr))
        
        if src in visited:
          visited.remove(src)
        return len(visited)
      
      def cmptr(a, b):
        if a[0] != b[0]:
          return a[0] - b[0]
        return -(a[1] - b[1])

      return min(
        [(dikjstra(n), n) for n in adj_list.keys()],
        key=functools.cmp_to_key(cmptr)
      )[1]