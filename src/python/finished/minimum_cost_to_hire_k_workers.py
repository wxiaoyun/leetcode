import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
      n = len(wage)
      # rate of each worker in the group = max rate of workers in the group
      # total paid = sum(rate_max * quantity_i)

      # we keep an pq of k workers
      # And we continuously remove the worker with the highest rate

      # List[Tuple[Quantity, Rate, Index]]
      worker = [(quality[i], wage[i] / quality[i]) for i in range(n)]
      worker.sort()

      pq = [] # max heap wrt rate
      total_quantity = 0
      for i in range(k):
        qty, rt = worker[i]
        total_quantity += qty
        heapq.heappush(pq, (-rt, qty))
      
      best = total_quantity * -pq[0][0]
      for i in range(k, n):
        qty, rt = worker[i]
        total_quantity += qty
        heapq.heappush(pq, (-rt, qty)) # Add new worker

        _, qty = heapq.heappop(pq) # Remove worker with highest rate
        total_quantity -= qty # Remove his work

        best = min(best, total_quantity * -pq[0][0]) # Update total paid
      return best


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        rate_quality = [(wage[i]/quality[i], quality[i]) for i in range(len(wage))]
        rate_quality.sort(key=lambda x: x[0])

        pq = []
        min_cost = float('inf')
        cur_total_quality = 0
        
        for (rate, quality) in rate_quality:
            heapq.heappush(pq, -quality)
            cur_total_quality += quality

            if len(pq) == k+1:
                popped = heapq.heappop(pq)
                cur_total_quality += popped # quality in pq is negative

            if len(pq) == k:
                min_cost = min(min_cost, cur_total_quality*rate)

        return min_cost