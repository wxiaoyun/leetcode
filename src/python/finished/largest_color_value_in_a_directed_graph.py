from typing import List

# https://leetcode.com/problems/largest-color-value-in-a-directed-graph


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        adj_list = [[] for _ in range(N)]
        pointer_count = [0] * N
        for u, v in edges:
            adj_list[u].append(v)
            pointer_count[v] += 1

        # 0. Find roots
        roots = []
        for i, c in enumerate(pointer_count):
            if c == 0:
                roots.append(i)

        no_ptrs = roots[:]
        while no_ptrs:
            r = no_ptrs.pop()
            for nb in adj_list[r]:
                pointer_count[nb] -= 1
                if pointer_count[nb] == 0:
                    no_ptrs.append(nb)

        if sum(pointer_count) != 0:
            return -1

        # 2. DFS to find the largest color
        dp = {}

        def dfs_find(cur: int) -> list:
            if cur in dp:
                return dp[cur]

            best = [0] * 26
            cidx = ord(colors[cur]) - ord("a")
            best[cidx] = 1

            for nb in adj_list[cur]:
                child_best = dfs_find(nb)
                for i, cnt in enumerate(child_best):
                    best[i] = max(best[i], cnt + (1 if i == cidx else 0))

            dp[cur] = best
            return best

        best = 0
        for r in roots:
            best = max(best, max(dfs_find(r)))

        return best
