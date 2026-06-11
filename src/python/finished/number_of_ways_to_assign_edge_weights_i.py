from collections import deque
from typing import List

# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

MOD = int(1e9) + 7
cache = [-1] * int(1e5)


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    if cache[n] > 0:
        return cache[n]
    cache[n] = (n * factorial(n - 1)) % MOD
    return cache[n]


def nCr(n: int, r: int) -> int:
    top = factorial(n)
    bot = (factorial(r) * factorial(n - r)) % MOD
    # Fermat's Little Theorem for Modular inverse
    return (top * pow(bot, MOD - 2, MOD)) % MOD


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj_list = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        frontier = deque([1])
        max_depth = -1
        visited = set()
        while frontier:
            l = len(frontier)
            for _ in range(l):
                node = frontier.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nb in adj_list[node]:
                    if nb in visited:
                        continue
                    frontier.append(nb)
            max_depth += 1

        # odd path cost = (2k + 1) odd_path + n * even_path

        n_ways = 0
        # print(max_depth)
        for i in range(1, max_depth + 1, 2):
            n_ways += nCr(max_depth, i)
            n_ways %= MOD
            # print(i, n_ways)

        return n_ways
