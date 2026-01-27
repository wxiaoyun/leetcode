import heapq
from typing import List

# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, 2 * w))

        visited = set()
        pq = [(0, 0)]
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)

            if node == n - 1:
                return cost

            for nb, w in adj_list[node]:
                if nb in visited:
                    continue
                heapq.heappush(pq, (cost + w, nb))

        return -1
