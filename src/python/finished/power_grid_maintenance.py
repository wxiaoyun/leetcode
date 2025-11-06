from typing import List
import heapq


# https://leetcode.com/problems/power-grid-maintenance/


class UF:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * (n)

    def find(self, n: int) -> int:
        p = self.parent[n]
        if p == n:
            return p

        pp = self.find(p)
        self.parent[n] = pp
        return pp

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


# Backwards processing
class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        uf = UF(c + 1)
        for u, v in connections:
            uf.union(u, v)

        first_offlines = {}
        offlines = set()
        OFFLINE = 2
        for i, (ty, sta) in enumerate(queries):
            if ty == OFFLINE:
                offlines.add(sta)
                first_offlines.setdefault((ty, sta), i)

        grp_min = {}
        for n in range(c + 1):
            if n in offlines:
                continue

            grp = uf.find(n)
            minn = grp_min.setdefault(grp, n)
            grp_min[grp] = min(minn, n)

        ans = []
        for i in reversed(range(len(queries))):
            ty, sta = queries[i]
            if ty == OFFLINE:
                if first_offlines[(ty, sta)] != i:
                    continue

                offlines.remove(sta)

                grp = uf.find(sta)
                minn = grp_min.setdefault(grp, sta)
                grp_min[grp] = min(minn, sta) if minn > 0 else sta
                continue

            if sta not in offlines:
                ans.append(sta)
                continue

            grp = uf.find(sta)
            ans.append(grp_min.setdefault(grp, -1))

        ans.reverse()
        return ans


# Forward heap construction
class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        uf = UF(c + 1)
        for u, v in connections:
            uf.union(u, v)

        heaps = {}
        offlines = {}
        for n in range(c + 1):
            grp = uf.find(n)
            heaps.setdefault(grp, []).append(n)

        for g in heaps.keys():
            heapq.heapify(heaps[g])

        ans = []
        for ty, sta in queries:
            grp = uf.find(sta)

            offline = offlines.setdefault(grp, set())
            if ty == 2:
                offline.add(sta)
                continue

            assert ty == 1

            if sta not in offline:
                ans.append(sta)
                continue

            heap = heaps.setdefault(grp, [grp])
            while heap and heap[0] in offline:
                heapq.heappop(heap)

            ans.append(heap[0] if heap else -1)

        return ans
