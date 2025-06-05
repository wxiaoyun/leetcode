# https://leetcode.com/problems/lexicographically-smallest-equivalent-string


class UF:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [1] * size
        return None

    def find(self, a: int) -> int:
        ap = self.parent[a]
        if a == ap:
            return a

        app = self.find(ap)
        self.parent[a] = app
        return app

    def union(self, a: int, b: int) -> None:
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return None

        apr = self.rank[ap]
        bpr = self.rank[bp]
        if apr < bpr:
            self.rank[bp] += apr
            self.parent[ap] = bp
        else:
            self.rank[ap] += bpr
            self.parent[bp] = ap
        return None


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def ordd(ch: str) -> int:
            return ord(ch) - ord("a")

        uf = UF(26)
        for n in range(len(s1)):
            a = ordd(s1[n])
            b = ordd(s2[n])
            uf.union(a, b)

        smallest = list(range(26))  # by classification
        for i in range(26):
            p = uf.find(i)
            smallest[p] = min(smallest[p], i)

        def get_smallest(ch: str) -> str:
            i = ordd(ch)
            p = uf.find(i)
            sm = smallest[p]
            return chr(ord("a") + sm)

        return "".join([get_smallest(s) for s in baseStr])
