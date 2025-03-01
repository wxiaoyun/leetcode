from collections import defaultdict
import heapq
from typing import List

# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        adj1 = defaultdict(list)
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        adj2 = defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def get_diameter(adj, cur, par):
            diam = -1
            child_depths = [0, 0]

            for nb in adj[cur]:
                if nb == par:
                    continue

                diam_est, depth = get_diameter(adj, nb, cur)
                diam = max(diam, diam_est)
                heapq.heappush(child_depths, depth)
                heapq.heappop(child_depths)

            diam = max(diam, sum(child_depths))
            return diam, 1 + max(child_depths)

        diam_a, _ = get_diameter(adj1, 0, -1)
        diam_b, _ = get_diameter(adj2, 0, -1)
        diam_new = (diam_a + 1) // 2 + (diam_b + 1) // 2 + 1
        return max(diam_a, diam_b, diam_new)

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        adj1 = defaultdict(list)
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        adj2 = defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def diameter(adj, cur, par) -> int:
            diam = 0
            child_max_depth = [0, 0]

            for nb in adj[cur]:
                if nb != par:
                    nb_diam, nb_depth = diameter(adj, nb, cur)

                    diam = max(diam, nb_diam)

                    heapq.heappush(child_max_depth, nb_depth)
                    heapq.heappop(child_max_depth)

            diam = max(diam, sum(child_max_depth))
            return diam, 1 + max(child_max_depth)

        dia1, _ = diameter(adj1, 0, -1)
        dia2, _ = diameter(adj2, 0, -1)
        return max(dia1, dia2, (dia1 + 1) // 2 + (dia2 + 1) // 2 + 1)
