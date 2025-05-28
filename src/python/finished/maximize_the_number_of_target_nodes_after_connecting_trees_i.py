from typing import List


# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
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

        # calculate k target for each node in tree 1
        # calculate (k-1) target for each node in tree 2
        def dfs(
            adj_list: List[List[int]],
            target: int,
            dp: List[int],
            src: int,
            cur: int,
            par: int,
            depth: int,
        ) -> None:
            if depth <= target:
                dp[src] += 1
            else:
                return

            for nb in adj_list[cur]:
                if nb == par:
                    continue
                dfs(adj_list, target, dp, src, nb, cur, depth + 1)

        t1_dp = [0] * N
        for n in range(N):
            dfs(adj_list1, k, t1_dp, n, n, -1, 0)

        t2_dp = [0] * M
        for m in range(M):
            dfs(adj_list2, k - 1, t2_dp, m, m, -1, 0)
        t2_best = max(t2_dp) if len(t2_dp) else 0

        ans = [0] * N
        for n in range(N):
            ans[n] = t1_dp[n] + t2_best
        return ans
