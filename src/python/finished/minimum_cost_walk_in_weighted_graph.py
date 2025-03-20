from typing import List

# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph


class UF:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.weight = [(1 << 32) - 1] * n

    def union(self, a: int, b: int, w: int) -> None:
        ap = self.find(a)
        bp = self.find(b)

        apr = self.rank[ap]
        bpr = self.rank[bp]

        if apr > bpr:
            self.parent[bp] = ap
            if ap != bp:
                self.rank[ap] += bpr
            self.weight[ap] &= self.weight[bp] & w

        else:
            self.parent[ap] = bp
            if ap != bp:
                self.rank[bp] += apr
            self.weight[bp] &= self.weight[ap] & w

        return None

    def find(self, a: int, w: int | None = None) -> int:
        p = self.parent[a]
        if p != a:
            self.parent[a] = self.find(p)
        return self.parent[a]

    def get_weight(self, a: int) -> int:
        return self.weight[self.find(a)]

    def __str__(self) -> str:
        return f"P: {self.parent}\nR: {self.rank}\nW: {self.weight}\n"


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        uf = UF(n)

        for u, v, w in edges:
            uf.union(u, v, w)

        res = [-1] * len(query)
        for i, (a, b) in enumerate(query):
            if uf.find(a) != uf.find(b):
                continue

            res[i] = uf.get_weight(a)
        return res
