from typing import List

# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        N = n + 1
        INF = 1 << 64
        uf_par = list(range(N))
        uf_rank = [1] * (N)
        uf_min = [INF] * N

        def find(a: int) -> int:
            ap = uf_par[a]
            if ap != a:
                app = find(ap)
                uf_par[a] = app
                uf_min[a] = uf_min[app]
            return uf_par[a]

        def union(a: int, b: int, mn: int):
            ap, bp = find(a), find(b)
            apr, bpr = uf_rank[ap], uf_rank[bp]
            if apr > bpr:
                uf_par[bp] = ap
                uf_rank[ap] += bpr
            else:
                uf_par[ap] = bp
                uf_rank[bp] += apr
            new_min = min(uf_min[a], uf_min[ap], uf_min[b], uf_min[bp], mn)
            uf_min[ap] = new_min
            uf_min[bp] = new_min
            return None

        def cmp_min(cmp: int) -> int:
            find(cmp)
            return uf_min[cmp]

        for a, b, d in roads:
            union(a, b, d)

        cmp_a, cmp_b = find(1), find(n)
        # print(uf_par)
        assert cmp_a == cmp_b
        return cmp_min(cmp_a)
