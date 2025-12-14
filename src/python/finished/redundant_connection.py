from typing import List

# https://leetcode.com/problems/redundant-connection/


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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for a, b in edges:
            n = max(n, a, b)

        redundant = []
        uf = UF(n + 1)
        for a, b in edges:
            if uf.find(a) == uf.find(b):
                redundant = [a, b]
                continue

            uf.union(a, b)
        return redundant


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, a: int, b: int) -> None:
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return None

        ar = self.rank[ap]
        br = self.rank[bp]

        if ar < br:
            self.parent[ap] = bp
        elif ar > br:
            self.parent[bp] = ap
        else:
            self.parent[bp] = ap
            self.rank[ap] += 1

        return None

    def find(self, a: int) -> int:
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 0

        p = self.parent[a]
        if p == a:
            return p

        self.parent[a] = self.find(p)
        return self.parent[a]

    def same_set(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e = None

        uf = UF()
        for a, b in edges:
            if uf.same_set(a, b):
                e = [a, b]
                continue
            uf.union(a, b)
        return e
