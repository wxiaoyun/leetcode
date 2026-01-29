import heapq
from typing import Dict, List

# https://leetcode.com/problems/minimum-cost-to-convert-string-i/


# O(n), use floyd-warshall to precompute min cost between characters
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        all_chars = list(source)
        all_chars.extend(list(target))
        all_chars.extend(original)
        all_chars.extend(changed)
        all_chars = set(all_chars)

        cost_map: Dict[str, Dict[str, int]] = {
            i: {j: float("inf") for j in all_chars} for i in all_chars
        }

        for c in all_chars:
            cost_map[c][c] = 0
        for i in range(len(original)):
            cost_map[original[i]][changed[i]] = min(
                cost_map[original[i]][changed[i]], cost[i]
            )

        for k in all_chars:
            for i in all_chars:
                for j in all_chars:
                    cost_map[i][j] = min(
                        cost_map[i][j], cost_map[i][k] + cost_map[k][j]
                    )

        total_cost = 0

        for i in range(len(source)):
            cst = cost_map[source[i]][target[i]]
            if cst == float("inf"):
                return -1
            total_cost += cst

        return total_cost


# O(n), use dijkstra to precompute min cost between characters
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 1 << 31
        adj_list = [[INF] * 26 for _ in range(26)]
        n = len(original)
        for i in range(n):
            u, v, c = original[i], changed[i], cost[i]
            x, y = ord(u) - ord("a"), ord(v) - ord("a")
            adj_list[x][y] = min(adj_list[x][y], c)

        for src in range(26):
            visited = set()
            pq = [(0, src)]
            while pq:
                c, i = heapq.heappop(pq)
                if i in visited:
                    continue
                visited.add(i)

                adj_list[src][i] = min(adj_list[src][i], c)

                for j in range(26):
                    if j in visited:
                        continue
                    heapq.heappush(pq, (c + adj_list[i][j], j))

        total_cost = 0
        for i in range(len(source)):
            src = ord(source[i]) - ord("a")
            dst = ord(target[i]) - ord("a")

            if adj_list[src][dst] == INF:
                return -1

            total_cost += adj_list[src][dst]
        return total_cost


# TLE: O(nlogn), dijkstra
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 1 << 31
        adj_list = [[INF] * 26 for _ in range(26)]
        n = len(original)
        for i in range(n):
            u, v, c = original[i], changed[i], cost[i]
            x, y = ord(u) - ord("a"), ord(v) - ord("a")
            adj_list[x][y] = min(adj_list[x][y], c)

        visited = set()
        # List<(cost, index, cur_char)>, where source[:i] is converted to target[:i] with cost c
        pq = [(0, 0, -1)]
        while pq:
            c, i, j = heapq.heappop(pq)
            if i >= len(source):
                return c

            if j < 0:
                j = ord(source[i]) - ord("a")
            node = (i, j)
            if node in visited:
                continue
            visited.add(node)

            if chr(j + ord("a")) == target[i]:
                heapq.heappush(pq, (c, i + 1, -1))
                continue

            for k in range(26):
                if adj_list[j][k] == INF:
                    continue
                if (i, k) in visited:
                    continue
                heapq.heappush(pq, (c + adj_list[j][k], i, k))

        return -1
