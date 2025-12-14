from typing import List

# https://neetcode.io/problems/count-connected-components/


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.component = n

    def find(self, a: int) -> int:
        if a == self.parent[a]:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int) -> None:
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return None

        apr, bpr = self.rank[ap], self.rank[bp]
        if apr > bpr:
            self.parent[bp] = ap
            self.rank[apr] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bpr] += apr

        self.component -= 1
        return None


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.component
