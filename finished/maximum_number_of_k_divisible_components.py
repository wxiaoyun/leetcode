from typing import List, Tuple

# https://leetcode.com/problems/maximum-number-of-k-divisible-components/


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj_list = [[] for _ in range(len(values))]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        split_count = 0

        def dfs(adj, cur, par):
            nonlocal split_count

            nbs = []
            for nb in adj[cur]:
                if nb != par:
                    nbs.append(nb)

            sub_total = values[cur]
            for nb in nbs:
                sub_total += dfs(adj, nb, cur)

            if sub_total % k == 0:
                split_count += 1
                return 0

            return sub_total

        dfs(adj_list, 0, -1)
        return split_count

    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj_list = [[] for _ in range(len(values))]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        split_count = 0

        def dfs(n: int, parent: int) -> Tuple[bool, int]:
            nonlocal split_count

            nbs = []
            for nb in adj_list[n]:
                if nb != parent:
                    nbs.append(nb)

            is_leaf = len(nbs) == 0
            subtree_value = values[n]
            if not is_leaf:
                for nb in nbs:
                    is_valid, val = dfs(nb, n)
                    if is_valid:
                        continue
                    subtree_value += val

            if subtree_value % k == 0:
                split_count += 1
                return True, -1
            else:
                return False, subtree_value

        dfs(0, -1)
        return split_count
