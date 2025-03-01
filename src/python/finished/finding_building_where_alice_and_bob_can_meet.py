import heapq
from typing import List

# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        ans = [-1] * len(queries)
        qs = [[] for _ in range(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b or heights[b] > heights[a]:
                ans[i] = b
                continue

            qs[b].append((heights[a], i))

        pq = []
        for i, h in enumerate(heights):
            while pq and pq[0][0] < h:
                _, q_idx = heapq.heappop(pq)
                ans[q_idx] = i

            for el in qs[i]:
                heapq.heappush(pq, el)

        return ans

    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        # find the leftmost building that is shorter than both building a and building b
        ans = [-1] * len(queries)
        rem_queries = [[] for _ in heights]
        for i, (a, b) in enumerate(queries):
            if a == b:
                ans[i] = a
                continue

            if a > b:
                a, b = b, a
            # a <= b

            if heights[a] < heights[b]:
                ans[i] = b
                continue

            # heights[a] >= heights[b]
            rem_queries[b].append((heights[a], i))  # [max_height, i]

        qpq = []
        for i, h in enumerate(heights):
            while qpq and qpq[0][0] < h:
                _, q_idx = heapq.heappop(qpq)
                ans[q_idx] = i

            for q in rem_queries[i]:
                heapq.heappush(qpq, q)
        return ans
