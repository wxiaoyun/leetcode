from collections import defaultdict
from typing import List

# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/


# TLE, O(n) string slicing
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        all_node_set = set()
        all_node_set.update(original)
        all_node_set.update(changed)
        all_nodes = list(all_node_set)
        m = len(all_nodes)
        rev_idx = {s: i for i, s in enumerate(all_nodes)}

        INF = 1 << 63
        max_len = 0
        pair_wise_cost = [[INF] * m for _ in range(m)]
        for n in range(m):
            pair_wise_cost[n][n] = 0
        for i in range(len(original)):
            u, v = rev_idx[original[i]], rev_idx[changed[i]]
            pair_wise_cost[u][v] = min(pair_wise_cost[u][v], cost[i])
            max_len = max(max_len, len(original[i]))

        for c in range(m):
            for a in range(m):
                if pair_wise_cost[a][c] == INF:
                    continue
                for b in range(m):
                    pair_wise_cost[a][b] = min(
                        pair_wise_cost[a][b],
                        pair_wise_cost[a][c] + pair_wise_cost[c][b],
                    )

        dp = {}

        def compute(i: int) -> int:
            if i >= len(target):
                return 0

            if i in dp:
                return dp[i]

            best = INF

            if source[i] == target[i]:
                best = min(best, compute(i + 1))

            for j in range(i + 1, min(len(target), i + max_len) + 1):
                u, v = source[i:j], target[i:j]
                if not u in rev_idx or not v in rev_idx:
                    continue
                uidx, vidx = rev_idx[u], rev_idx[v]
                if pair_wise_cost[uidx][vidx] < INF:
                    best = min(best, pair_wise_cost[uidx][vidx] + compute(j))

            dp[i] = best
            return best

        mvs = compute(0)
        return mvs if mvs < INF else -1


# TLE due to O(n) string hash
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        all_node_set = set()
        all_node_set.update(original)
        all_node_set.update(changed)
        all_nodes = list(all_node_set)

        INF = 1 << 31
        max_len = 0
        pair_wise_cost = defaultdict(lambda: INF)
        for n in all_nodes:
            pair_wise_cost[(n, n)] = 0
        for i in range(len(original)):
            u, v = original[i], changed[i]
            pair_wise_cost[(u, v)] = min(pair_wise_cost[(u, v)], cost[i])
            max_len = max(max_len, len(u))

        m = len(all_nodes)
        for k in range(m):
            c = all_nodes[k]
            for j in range(m):
                b = all_nodes[j]
                for i in range(m):
                    a = all_nodes[i]
                    pair_wise_cost[(a, b)] = min(
                        pair_wise_cost[(a, b)],
                        pair_wise_cost[(a, c)] + pair_wise_cost[(c, b)],
                    )

        dp = {}

        def compute(i: int) -> int:
            if i >= len(target):
                return 0

            if i in dp:
                return dp[i]

            best = INF

            if source[i] == target[i]:
                best = min(best, compute(i + 1))

            for j in range(i + 1, min(len(target), i + max_len) + 1):
                u, v = source[i:j], target[i:j]
                if pair_wise_cost[(u, v)] < INF:
                    best = min(best, pair_wise_cost[(u, v)] + compute(j))

            dp[i] = best
            return best

        mvs = compute(0)
        return mvs if mvs < INF else -1
