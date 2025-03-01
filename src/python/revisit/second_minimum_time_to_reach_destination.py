# https://leetcode.com/problems/second-minimum-time-to-reach-destination

from collections import deque
import heapq
from typing import Dict, List, Set


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
      adj_list: Dict[int, Set[int]] = {
        i: set() for i in range(1, n+1)
      }

      for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)

      def calc_time(t: int) -> int:
        is_green = t % (2*change) < change
        return t+time if is_green else t-(t%change)+change + time
      
      d1 = [float('inf')] * (n+1)
      d2 = [float('inf')] * (n+1)
      freq = [0] * (n+1)
      pq = [(0, 1)] # time, city

      while pq:
        t, c = heapq.heappop(pq)

        freq[c] += 1

        if c == n and freq[c] == 2:
          return t

        for ngbr in adj_list[c]:
          if freq[ngbr] >= 2:
            continue

          new_time = calc_time(t)

          if new_time < d1[ngbr]:
            d2[ngbr] = d1[ngbr]
            d1[ngbr] = new_time
          elif new_time > d1[ngbr] and new_time < d2[ngbr]:
            d2[ngbr] = new_time
          else:
            continue

          heapq.heappush(pq, (new_time, ngbr))
      
      return -1