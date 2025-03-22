from typing import List

# https://leetcode.com/problems/count-the-number-of-complete-components


class UF:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def union(self, a: int, b: int) -> None:
        ap = self.find(a)
        bp = self.find(b)

        if ap == bp:
            return None

        apr = self.rank[ap]
        bpr = self.rank[bp]

        if apr > bpr:
            self.parent[bp] = ap
            self.rank[ap] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bp] += apr

        return None

    def find(self, a: int) -> int:
        p = self.parent[a]
        if p != a:
            self.parent[a] = self.find(p)
        return self.parent[a]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)

        vertex_degree = [0] * n
        for a, b in edges:
            uf.union(a, b)
            vertex_degree[a] += 1
            vertex_degree[b] += 1

        comp_deg = {}
        for i in range(n):
            comp = uf.find(i)

            if comp not in comp_deg:
                comp_deg[comp] = float("inf")

            comp_deg[comp] = min(comp_deg[comp], vertex_degree[i])

        count = 0
        for comp, min_deg in comp_deg.items():
            if uf.rank[comp] == min_deg + 1:
                count += 1
        return count
