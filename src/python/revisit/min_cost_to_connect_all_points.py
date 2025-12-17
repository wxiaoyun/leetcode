import heapq
from typing import List


# Prim's algo
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        visited = set()
        pq = [(0, points[0][0], points[0][1])]
        while pq:
            dist, x, y = heapq.heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            total_cost += dist

            for xx, yy in points:
                if (xx, yy) in visited:
                    continue

                dist = abs(xx - x) + abs(yy - y)
                heapq.heappush(pq, (dist, xx, yy))

        return total_cost


# Krustal's algo
class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a: int) -> int:
        if a == self.parent[a]:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return

        apr, bpr = self.rank[a], self.rank[b]
        if apr > bpr:
            self.parent[bp] = ap
            self.rank[ap] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bp] += apr
        return


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i, j))

        uf = UF(n)
        total_cost = 0

        edges.sort()
        for w, a, b in edges:
            if uf.find(a) == uf.find(b):
                continue

            uf.union(a, b)
            total_cost += w
        return total_cost
