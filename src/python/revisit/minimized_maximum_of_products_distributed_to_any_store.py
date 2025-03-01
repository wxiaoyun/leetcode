import heapq
import math
from typing import List

# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # if x can distribute, then for any x_i > x, x_i can also distribute
        # Thus, x_target <= x if can distribute
        def can_distribute(x: int) -> bool:
          count = 0
          for q in quantities:
            cur = q
            while cur > 0:
              cur -= x
              count += 1
              if count > n:
                return False
          return True
        
        lo, hi = 0, max(quantities)

        # invariant: lo <= x_target <= hi
        while lo < hi:
          mi = lo + (hi - lo) // 2
          # x_target <= x
          if can_distribute(mi):
            hi = mi
          # x < x_target
          else:
            lo = mi + 1
        return lo

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        pq = [(-q, 1, q) for q in quantities]
        heapq.heapify(pq)

        k = len(quantities)
        while k < n:
            neg_ratio, nstores, total = heapq.heappop(pq)
            nstores += 1
            k += 1

            heapq.heappush(pq, (-1 * (total / nstores), nstores, total))

        return math.ceil(-1 * pq[0][0])
