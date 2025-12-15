import heapq
from typing import List

# https://leetcode.com/problems/k-closest-points-to-origin


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(pq, (-dist, x, y))
            if len(pq) > k:
                heapq.heappop(pq)

        return [(x, y) for _, x, y in pq]
