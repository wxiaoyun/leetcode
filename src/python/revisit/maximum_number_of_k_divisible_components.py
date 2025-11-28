from typing import List
from collections import deque

# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [set() for _ in range(n)]
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        subtree_sum = values[:]
        leaves = deque()
        for node in range(n):
            if len(adj_list[node]) <= 1:
                leaves.append(node)

        components = 0
        while leaves:
            l = leaves.popleft()

            nbr_set = adj_list[l]
            assert len(nbr_set) <= 1

            parent = None
            if nbr_set:
                parent = nbr_set.pop()
            else:
                assert (subtree_sum[l] % k) == 0
                components += 1
                break

            if (subtree_sum[l] % k) == 0:
                components += 1
            else: # merge with parent
                subtree_sum[parent] += subtree_sum[l]

            adj_list[parent].remove(l)
            if len(adj_list[parent]) == 1:
                leaves.append(parent)

        return components



# O(n^3) brute force solution, TLE
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # since the graph is a tree, removing any edge will separate the graph

        # Suppose the graph is split into 2 components A and B
        # sum of each component are divisible by k. We can recursively call on each of the sub components

        adj_list = [[] for _ in range(n)]
        removed = [False] * len(edges)
        for i, (u, v) in enumerate(edges):
            adj_list[u].append((v, i))
            adj_list[v].append((u, i))

        def find_reachable(node: int) -> set:
            q = deque([node])
            visited = set()
            while q:
                m = q.popleft()
                if m in visited:
                    continue
                visited.add(m)

                for (nb, i) in adj_list[m]:
                    if removed[i]:
                        continue
                    q.append(nb)
            return visited

        def helper(reachable: set) -> int:
            try_deleted = set()
            max_comp = 1
            for u in reachable:
                for (v, i) in adj_list[u]:
                    if v not in reachable:
                        continue
                    if removed[i] or i in try_deleted:
                        continue
                    try_deleted.add(i)

                    removed[i] = True
                    u_reachable = find_reachable(u)
                    u_sum = 0
                    for uu in u_reachable:
                        u_sum += values[uu]
                    u_ok = (u_sum % k) == 0
                    if u_ok:
                        v_reachable = find_reachable(v)
                        max_comp = max(max_comp, helper(u_reachable) + helper(v_reachable))
                    removed[i] = False

            return max_comp

        return helper(set(range(n)))
