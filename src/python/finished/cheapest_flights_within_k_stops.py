import heapq
from typing import List

# https://leetcode.com/problems/cheapest-flights-within-k-stops


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_list = [[] for _ in range(n)]
        for fr, to, pr in flights:
            adj_list[fr].append((to, pr))

        visited = set()
        pq = [(0, -1, src)]
        while pq:
            price, stops, node = heapq.heappop(pq)
            key = (node, stops)
            if key in visited:
                continue
            visited.add(key)

            if stops > k:
                continue

            if node == dst:
                return price

            for nb, pr in adj_list[node]:
                heapq.heappush(pq, (price + pr, stops + 1, nb))

        return -1
