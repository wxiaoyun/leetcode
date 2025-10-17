from typing import List

# https://leetcode.com/problems/connecting-cities-with-minimum-cost/


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def union(self, a: int, b: int):
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return None

        apr, bpr = self.rank[ap], self.rank[bp]
        if apr > bpr:
            self.parent[bp] = ap
            self.rank[ap] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bp] += apr
        return None

    def find(self, a: int) -> int:
        if a == self.parent[a]:
            return a

        ap = self.parent[a]
        app = self.find(ap)
        if ap == app:
            return ap

        self.parent[a] = app
        return app


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda t: t[2])

        total_cost = 0
        edges = 0
        uf = UF(n)
        for x, y, cost in connections:
            x, y = x - 1, y - 1
            if uf.find(x) == uf.find(y):
                continue

            uf.union(x, y)
            total_cost += cost
            edges += 1

        return -1 if edges != n - 1 else total_cost
