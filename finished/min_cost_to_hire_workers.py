# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import heapq
from typing import List

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
