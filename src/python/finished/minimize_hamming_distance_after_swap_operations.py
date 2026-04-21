from collections import Counter
from typing import List

# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a: int) -> int:
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return

        apr, bpr = self.rank[ap], self.rank[bp]
        if apr > bpr:
            self.rank[ap] += bpr
            self.parent[bp] = ap
        else:
            self.rank[bp] += apr
            self.parent[ap] = bp
        return None


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        # goal: minimise number of elements that are different

        # we can use union find to determine which indices are connected (by some sequence of swaps)
        # In any such connected component, we can swap any two element

        # the problem reduces to:
        # 1. Elements not in any component: count difference directly
        # 2. Elements in a connected component: calculate the number of overlapping elements
        # 3. Sum the results and return

        n = len(source)
        assert n == len(target)
        uf = UF(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        components = {}
        for i in range(n):
            icomp = uf.find(i)
            components.setdefault(icomp, [])
            components[icomp].append(i)
        # print(components)

        def calc_overlap(indices: List[int]) -> int:
            src_cnt = Counter(source[i] for i in indices)
            tgt_cnt = Counter(target[i] for i in indices)
            return sum(min(src_cnt[k], tgt_cnt[k]) for k in src_cnt.keys())

        return n - sum(calc_overlap(indices) for indices in components.values())
