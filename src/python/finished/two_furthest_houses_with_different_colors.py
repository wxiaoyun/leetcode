import heapq
from typing import List

# https://leetcode.com/problems/two-furthest-houses-with-different-colors


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        INF = 1 << 32
        cleft = {}
        cright = {}

        for i, c in enumerate(colors):
            cleft[c] = min(i, cleft.setdefault(c, INF))
            cright[c] = max(i, cright.setdefault(c, -1))
        assert len(cleft) >= 2

        left_pq = []
        for c, i in cleft.items():
            heapq.heappush(left_pq, (-i, c))
            if len(left_pq) > 2:
                heapq.heappop(left_pq)

        right_pq = []
        for c, i in cright.items():
            heapq.heappush(right_pq, (i, c))
            if len(right_pq) > 2:
                heapq.heappop(right_pq)

        if left_pq[-1][1] != right_pq[-1][1]:
            return right_pq[-1][0] - (-left_pq[-1][0])

        return max(
            right_pq[0][0] - (-left_pq[-1][0]),
            right_pq[-1][0] - (-left_pq[0][0]),
        )
