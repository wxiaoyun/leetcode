from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, a: int) -> int:
        ap = self.parent.setdefault(a, a)
        if ap == a:
            return a

        app = self.find(ap)
        self.parent[a] = app
        return app

    def union(self, a: int, b: int) -> None:
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return

        apr, bpr = self.rank.setdefault(ap, 1), self.rank.setdefault(bp, 1)
        if apr > bpr:
            self.parent[bp] = ap
            self.rank[ap] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bp] += apr
        return


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        uf = UF()
        for n in nums:
            if n - 1 in seen:
                uf.union(n - 1, n)
            if n + 1 in seen:
                uf.union(n, n + 1)
            seen.add(n)

        return max(uf.rank.values() if uf.rank else [1])
