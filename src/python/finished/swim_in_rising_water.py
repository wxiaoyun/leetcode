import heapq
from typing import List

# https://leetcode.com/problems/swim-in-rising-water/


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        t = 0
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        while pq:
            time, r, c = heapq.heappop(pq)
            visited.add((r, c))
            t = max(t, time)

            if r == m - 1 and c == n - 1:
                return t

            for rr, cc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                if (rr, cc) in visited:
                    continue

                heapq.heappush(pq, (grid[rr][cc], rr, cc))

        return -1


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dest = (R - 1, C - 1)
        visited = set()

        pq = [(grid[0][0], 0, 0)]
        while pq:
            t, r, c = heapq.heappop(pq)

            node = (r, c)
            if node in visited:
                continue
            visited.add(node)

            if node == dest:
                return t

            for rr, cc in [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]:
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue

                tt = grid[rr][cc]
                heapq.heappush(pq, (max(tt, t), rr, cc))

        return -1
