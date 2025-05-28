from typing import List
from collections import defaultdict


# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        adj_list1 = defaultdict(list)
        adj_list2 = defaultdict(list)

        N = 0
        for u, v in edges1:
            N = max(N, u, v)
            adj_list1[u].append(v)
            adj_list1[v].append(u)
        N += 1

        M = 0
        for u, v in edges2:
            M = max(M, u, v)
            adj_list2[u].append(v)
            adj_list2[v].append(u)
        M += 1

        # calculate k target for each node in tree 1
        # calculate (k-1) target for each node in tree 2
        def dfs(
            adj_list: dict,
            target: int,
            dp: dict,
            src: int,
            cur: int,
            par: int,
            depth: int,
        ) -> None:
            if depth <= target:
                dp[src] += 1

            for nb in adj_list[cur]:
                if nb == par:
                    continue
                dfs(adj_list, target, dp, src, nb, cur, depth + 1)

        t1_dp = defaultdict(int)
        for n in range(N):
            dfs(adj_list1, k, t1_dp, n, n, -1, 0)

        t2_dp = defaultdict(int)
        for m in range(M):
            dfs(adj_list2, k - 1, t2_dp, m, m, -1, 0)

        t2_best = max(t2_dp.values()) if len(t2_dp) else 0

        ans = [0] * N
        for n in range(N):
            ans[n] = t1_dp[n] + t2_best
        return ans
