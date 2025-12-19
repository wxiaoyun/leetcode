import heapq
from typing import List

# https://leetcode.com/problems/find-all-people-with-secret


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for x, y, t in meetings:
            adj_list[x].append((y, t))
            adj_list[y].append((x, t))

        visited = set()
        time = 0
        pq = [(0, 0), (0, firstPerson)]
        while pq:
            t, p = heapq.heappop(pq)
            if t < time:
                continue
            time = t

            if p in visited:
                continue
            visited.add(p)

            for nb, tt in adj_list[p]:
                heapq.heappush(pq, (tt, nb))

        return list(visited)
