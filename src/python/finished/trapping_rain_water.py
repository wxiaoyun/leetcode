import heapq
from typing import List

# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        lowest_boundary = 0

        n = len(height)
        visited = set()
        bound_pq = []
        heapq.heappush(bound_pq, (height[0], 0))
        heapq.heappush(bound_pq, (height[n - 1], n - 1))

        vol = 0
        while bound_pq:
            h, i = heapq.heappop(bound_pq)
            if i in visited:
                continue
            visited.add(i)

            vol += max(0, lowest_boundary - h)
            lowest_boundary = max(lowest_boundary, h)

            for d in [-1, 1]:
                j = i + d
                if j < 0 or j >= n:
                    continue
                heapq.heappush(bound_pq, (height[j], j))

        return vol
