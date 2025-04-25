from typing import List

# https://leetcode.com/problems/sum-of-distances-in-tree


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        res = [0] * n
        subtree_count = [0] * n

        def dfs(node: int, depth: int, parent: int) -> None:
            res[0] += depth

            for nb in adj_list[node]:
                if nb == parent:
                    continue

                dfs(nb, depth + 1, node)
                subtree_count[node] += subtree_count[nb]

            subtree_count[node] += 1

        dfs(0, 0, -1)

        def dfs_diff(node: int, parent: int) -> None:
            for nb in adj_list[node]:
                if nb == parent:
                    continue

                nodes_closer = subtree_count[nb]
                nodes_further = n - subtree_count[nb]
                res[nb] = res[node] - nodes_closer + nodes_further

                dfs_diff(nb, node)

        dfs_diff(0, -1)

        return res
