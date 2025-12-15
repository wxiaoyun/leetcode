import heapq
from typing import List

# https://leetcode.com/problems/network-delay-time


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, w in times:
            adj_list[u - 1].append((v - 1, w))

        estimates = [float("inf")] * n
        visited = set()
        pq = [(0, k - 1)]
        while pq:
            t, node = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)
            estimates[node] = t

            for nb, w in adj_list[node]:
                heapq.heappush(pq, (t + w, nb))

        min_t = max(estimates)
        return min_t if min_t != float("inf") else -1
