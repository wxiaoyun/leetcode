from typing import List, Optional


# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        N = len(edges1) + 1
        adj_list1 = [[] for _ in range(N)]
        for u, v in edges1:
            adj_list1[u].append(v)
            adj_list1[v].append(u)

        M = len(edges2) + 1
        adj_list2 = [[] for _ in range(M)]
        for u, v in edges2:
            adj_list2[u].append(v)
            adj_list2[v].append(u)

        def dfs(
            adj_list: List[List[int]],
            map: Optional[List[int]],
            dp: List[int],
            cur: int,
            par: int,
            depth: int,
        ) -> None:
            mod = depth % 2
            if map is not None:
                map[cur] = mod
            dp[mod] += 1

            for nb in adj_list[cur]:
                if nb == par:
                    continue
                dfs(adj_list, map, dp, nb, cur, depth + 1)

        t1_map = [0] * N
        t1_dp = [0, 0]
        dfs(adj_list1, t1_map, t1_dp, 0, -1, 0)

        t2_dp = [0, 0]
        dfs(adj_list2, None, t2_dp, 0, -1, 0)
        t2_best = max(t2_dp)

        ans = [0] * N
        for n in range(N):
            mod = t1_map[n]
            ans[n] = t1_dp[mod] + t2_best
        return ans
