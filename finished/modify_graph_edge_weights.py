# https://leetcode.com/problems/modify-graph-edge-weights/

from collections import defaultdict
import heapq
from typing import Dict, List, Tuple


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(adj_list: Dict[int, List[Tuple[int, int]]], src: int, dst: int) -> int:
          visited = set()
          pq = [(0, src)] 

          while pq:
            dist, cur_node = heapq.heappop(pq)

            if cur_node in visited:
              continue
            if cur_node == dst:
              return dist
            visited.add(cur_node)

            for nb, w in adj_list[cur_node]:
              if nb in visited:
                continue
              heapq.heappush(pq, (dist+w, nb))
          return float('inf')

        adj_list = defaultdict(list)
        for a, b, w in edges:
          if w < 0:
            continue
          adj_list[a].append((b, w))
          adj_list[b].append((a, w))
        shortest_unmodified = dijkstra(adj_list, source, destination)
        if shortest_unmodified < target:
          return [] # always a shorter path regardless of modification
        if shortest_unmodified == target:
          return [(a, b, w if w > 0 else int(2e9)) for a, b, w in edges]
        
        for i, (a, b, w) in enumerate(edges):
          if w > 0:
            continue
          
          edges[i][2] = 1
          adj_list[a].append((b, abs(w)))
          adj_list[b].append((a, abs(w)))

          modified_shortest = dijkstra(adj_list, source, destination)
          if modified_shortest <= target:
            edges[i][2] += target - modified_shortest
            for j in range(i+1, len(edges)):
              if edges[j][2] == -1:
                edges[j][2] = int(2e9)
            return edges
        return []