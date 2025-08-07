# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

from typing import List, Tuple, Callable
from collections import deque


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        collected = 0
        for i in range(n):
            collected += fruits[i][i]

        def compute(
            r: int,
            c: int,
            fruits: List[List[int]],
            moves: List[Tuple[int, int]],
            is_valid: Callable,
        ) -> int:
            n = len(fruits)
            for i in range(n):
                fruits[i][i] = 0

            q = deque([(r, c)])
            visited = set()
            while q:
                r, c = q.popleft()
                node = (r, c)
                if node in visited or not is_valid(node):
                    continue
                visited.add(node)

                for dr, dc in moves:
                    rr, cc = r + dr, c + dc
                    if min(rr, cc) < 0 or rr >= n or cc >= n:
                        continue
                    q.append((rr, cc))

                cur = fruits[r][c]
                for dr, dc in moves:
                    pr, pc = r - dr, c - dc
                    if (pr + pc) < n - 1:
                        continue
                    if min(pr, pc) < 0 or pr >= n or pc >= n:
                        continue

                    fruits[r][c] = max(fruits[r][c], fruits[pr][pc] + cur)

            return fruits[n - 1][n - 1]

        moves = [(1, -1), (1, 0), (1, 1)]
        is_valid = lambda x: x[0] <= x[1]
        collected += compute(0, n - 1, fruits, moves, is_valid)

        moves = [(-1, 1), (0, 1), (1, 1)]
        is_valid = lambda x: x[0] >= x[1]
        collected += compute(n - 1, 0, fruits, moves, is_valid)

        return collected
