# https://leetcode.com/problems/path-with-maximum-probability/

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i, (a, b) in enumerate(edges):
          prob = succProb[i]
          adj_list[a].append((b, prob))
          adj_list[b].append((a, prob))
        
        pq = [(-1, start_node)] # max heap
        visited = set()
        while pq:
          p, n = heapq.heappop(pq)
          p = -p

          if n in visited:
            continue
          if n == end_node:
            return p
          visited.add(n)

          for nb, nb_prob in adj_list[n]:
            if nb in visited:
              continue
            heapq.heappush(pq, (-p * nb_prob, nb))
        return 0