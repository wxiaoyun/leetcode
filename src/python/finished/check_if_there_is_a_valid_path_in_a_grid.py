from typing import List

# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid


TOP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


def leaves(ty: int, dir: int) -> bool:
    assert ty in list(range(1, 7)) and dir in list(range(4))

    if dir == TOP and ty in [2, 5, 6]:
        return True
    if dir == RIGHT and ty in [1, 4, 6]:
        return True
    if dir == DOWN and ty in [2, 3, 4]:
        return True
    if dir == LEFT and ty in [1, 3, 5]:
        return True
    return False


def accepts(ty: int, dir: int) -> bool:
    assert ty in list(range(1, 7)) and dir in list(range(4))

    if dir == DOWN and ty in [2, 5, 6]:
        return True
    if dir == LEFT and ty in [1, 4, 6]:
        return True
    if dir == TOP and ty in [2, 3, 4]:
        return True
    if dir == RIGHT and ty in [1, 3, 5]:
        return True
    return False


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        adj_list = [[] for _ in range(m * n)]

        for r, row in enumerate(grid):
            for c, ty in enumerate(row):
                idx = r * n + c

                for dir, rr, cc in [
                    (TOP, r - 1, c),
                    (RIGHT, r, c + 1),
                    (DOWN, r + 1, c),
                    (LEFT, r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= m or cc >= n:
                        continue

                    if leaves(ty, dir) and accepts(grid[rr][cc], dir):
                        adj_list[idx].append(rr * n + cc)

        stk = [0]
        visited = set()
        while stk:
            nd = stk.pop()
            if nd in visited:
                continue
            visited.add(nd)

            if nd == m * n - 1:
                return True

            for nb in adj_list[nd]:
                stk.append(nb)

        return False
