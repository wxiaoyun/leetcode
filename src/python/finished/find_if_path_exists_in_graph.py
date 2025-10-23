from typing import List

# https://leetcode.com/problems/find-if-path-exists-in-graph


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node == destination:
                return True
            for nb in adj_list[node]:
                stack.append(nb)
        return False
