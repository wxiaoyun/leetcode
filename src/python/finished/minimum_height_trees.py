from typing import List

# https://leetcode.com/problems/minimum-height-trees


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        in_deg = [0] * n
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            in_deg[a] += 1
            in_deg[b] += 1

        leaves = []
        for node, cnt in enumerate(in_deg):
            if cnt <= 1:
                leaves.append(node)

        visited = set()
        prev_frontier = []
        frontier = leaves[:]
        while frontier:
            prev_frontier = frontier[:]
            next_frontier = []

            while frontier:
                node = frontier.pop()
                visited.add(node)

                for nb in adj_list[node]:
                    if nb in visited:
                        continue

                    in_deg[nb] -= 1
                    if in_deg[nb] == 1:
                        next_frontier.append(nb)

            frontier = next_frontier

        return prev_frontier
