from typing import List

# https://leetcode.com/problems/find-closest-node-to-given-two-nodes


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)

        def dfs(edges: List[int], dist: List[int], n: int, depth: int = 0) -> None:
            if depth >= dist[n]:
                return None
            dist[n] = depth

            if edges[n] < 0:
                return None
            return dfs(edges, dist, edges[n], depth + 1)

        MAX = 1 << 32 - 1
        dist1 = [MAX] * N
        dfs(edges, dist1, node1)

        dist2 = [MAX] * N
        dfs(edges, dist2, node2)

        best, best_idx = MAX, -1
        for n in range(N):
            dist = max(dist1[n], dist2[n])
            if dist < best:
                best = dist
                best_idx = n
        return best_idx
