# https://leetcode.com/problems/minimum-score-after-removal-on-a-tree/

from typing import List


# Brute force TLE:
# Time O(E^2 * N)
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)

        def compute(nums: List[int], edges: List[List[int]]) -> int:
            adj_list = [[] for _ in range(N)]
            for a, b in edges:
                adj_list[a].append(b)
                adj_list[b].append(a)

            def dfs(
                nums: List[int], adj_list: List[List[int]], visited: set, node: int
            ) -> int:
                if node in visited:
                    return 0
                visited.add(node)

                res = nums[node]
                for nb in adj_list[node]:
                    res ^= dfs(nums, adj_list, visited, nb)
                return res

            visited = set()
            res = []
            for node in range(N):
                if node in visited:
                    continue
                res.append(dfs(nums, adj_list, visited, node))
            res.sort()
            return res[-1] - res[0]

        E = len(edges)
        edge_mut = {i: e for i, e in enumerate(edges)}
        best = float("inf")

        for i in range(E):
            del edge_mut[i]
            for j in range(i + 1, E):
                del edge_mut[j]
                best = min(best, compute(nums, list(edge_mut.values())))
                edge_mut[j] = edges[j]

            edge_mut[i] = edges[i]

        return best
