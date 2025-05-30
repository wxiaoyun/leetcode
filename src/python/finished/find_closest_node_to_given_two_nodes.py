from typing import List

# https://leetcode.com/problems/find-closest-node-to-given-two-nodes


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        adj_list = [[] for _ in range(N)]
        for u, v in enumerate(edges):
            if v < 0:
                continue
            adj_list[u].append(v)

        def dfs(
            adj_list: List[List[int]], dist: List[int], n: int, depth: int = 0
        ) -> None:
            if depth >= dist[n]:
                return None
            dist[n] = depth

            for nb in adj_list[n]:
                dfs(adj_list, dist, nb, depth + 1)
            return None

        MAX = 1 << 32 - 1
        dist1 = [MAX] * N
        dfs(adj_list, dist1, node1)

        dist2 = [MAX] * N
        dfs(adj_list, dist2, node2)

        best, best_idx = MAX, -1
        for n in range(N):
            dist = max(dist1[n], dist2[n])
            if dist < best:
                best = dist
                best_idx = n
        return best_idx
