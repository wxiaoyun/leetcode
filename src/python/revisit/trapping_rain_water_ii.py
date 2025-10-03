import heapq
from typing import List

# https://leetcode.com/problems/trapping-rain-water-ii/


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R = len(heightMap)
        C = len(heightMap[0])

        boundary = set()
        for r in range(R):
            boundary.add((r, 0))
            boundary.add((r, C - 1))
        for c in range(C):
            boundary.add((0, c))
            boundary.add((R - 1, c))

        boundary_pq = [(heightMap[r][c], r, c) for r, c in boundary]
        heapq.heapify(boundary_pq)

        volume = 0
        while boundary_pq:
            h, r, c = heapq.heappop(boundary_pq)

            for nbr in [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]:
                rr, cc = nbr
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue
                if nbr in boundary:
                    continue

                hh = heightMap[rr][cc]
                volume += max(0, h - hh)

                heapq.heappush(boundary_pq, (max(h, hh), rr, cc))
                boundary.add((rr, cc))

        return volume


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R = len(heightMap)
        C = len(heightMap[0])

        pq = []
        for i in range(R):
            cell = (heightMap[i][0], i, 0)
            heapq.heappush(pq, cell)
            cell = (heightMap[i][C - 1], i, C - 1)
            heapq.heappush(pq, cell)

        for j in range(C):
            cell = (heightMap[0][j], 0, j)
            heapq.heappush(pq, cell)
            cell = (heightMap[R - 1][j], R - 1, j)
            heapq.heappush(pq, cell)

        vol = 0
        min_barrier = 0
        visited = set()
        while pq:
            h, r, c = heapq.heappop(pq)

            cell = (r, c)
            if cell in visited:
                continue
            visited.add(cell)

            min_barrier = h

            for cell in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if cell in visited:
                    continue

                rr, cc = cell
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue

                nb_h = heightMap[rr][cc]
                vol += max(0, min_barrier - nb_h)
                heightMap[rr][cc] = max(min_barrier, nb_h)

                heapq.heappush(pq, (heightMap[rr][cc], rr, cc))
        return vol
