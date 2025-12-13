from typing import List

# https://neetcode.io/problems/valid-tree


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a: int) -> int:
        ap = self.parent[a]
        if ap == a:
            return ap

        app = self.find(ap)
        self.parent[a] = app
        return app

    def union(self, a: int, b: int) -> None:
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


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a connected, acyclic graph

        if n - 1 != len(edges):
            return False

        uf = UF(n)
        for a, b in edges:
            ap, bp = uf.find(a), uf.find(b)
            if ap == bp:
                # a cycle is formed since this union creates alternative path between a and b
                return False

            uf.union(a, b)
        return True
