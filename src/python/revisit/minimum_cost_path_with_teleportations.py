import heapq
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList

# https://leetcode.com/problems/minimum-cost-path-with-teleportations


# TLE
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        best_moves = defaultdict(lambda: k)
        moves = [SortedList(key=lambda t: grid[t[0]][t[1]]) for _ in range(k)]
        for r in range(n):
            for c in range(m):
                moves[0].add((r, c))

        pq = [(0, 0, 0, 0)]
        while pq:
            cost, mv, r, c = heapq.heappop(pq)
            prev_move = best_moves[(r, c)]
            if mv >= prev_move:
                continue

            best_moves[(r, c)] = mv
            if prev_move < k:
                moves[prev_move].remove((r, c))
            moves[mv].add((r, c))

            if r == n - 1 and c == m - 1:
                return cost

            for rr, cc in [(r, c + 1), (r + 1, c)]:
                if min(rr, cc) < 0 or rr >= n or cc >= m:
                    continue
                if mv >= best_moves[(rr, cc)]:
                    continue
                heapq.heappush(pq, (cost + grid[rr][cc], mv, rr, cc))

            if mv < k:
                for j in range(max(1, mv)):
                    i = moves[j].bisect_right((r, c))
                    for rr, cc in moves[j][:i]:
                        heapq.heappush(pq, (cost, mv + 1, rr, cc))

        return -1
