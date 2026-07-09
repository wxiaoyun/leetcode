from typing import List

# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        par = list(range(n))
        rank = [1] * n

        def find(a: int) -> int:
            ap = par[a]
            if ap != a:
                par[a] = find(ap)
            return par[a]

        def union(a: int, b: int):
            ap, bp = find(a), find(b)
            apr, bpr = rank[ap], rank[bp]

            if apr > bpr:
                par[bp] = ap
                rank[ap] += bpr
            else:
                par[ap] = bp
                rank[bp] += apr
            return None

        for idx in range(n - 1):
            i, j = idx, idx + 1
            if nums[j] - nums[i] > maxDiff:
                continue
            union(i, j)

        return [find(u) == find(v) for u, v in queries]
