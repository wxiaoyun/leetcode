# https://leetcode.com/problems/cyclically-rotating-a-grid

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ret = [[-1] * n for _ in range(m)]

        def rotate(offset: int, k: int) -> None:
            # D, L, L, L
            # D, ., ., U
            # D, ., ., U
            # R, R, R, U

            # move left col down
            mapping = []
            for r in range(offset, m - offset - 1):
                mapping.append((r, offset))

            # move bottom row right
            for c in range(offset, n - offset - 1):
                mapping.append((m - offset - 1, c))

            # move right col up
            for r in reversed(range(offset + 1, m - offset)):
                mapping.append((r, n - offset - 1))

            # move top row left
            for c in reversed(range(offset + 1, n - offset)):
                mapping.append((offset, c))

            # ---------------------------------------
            for i in range(len(mapping)):
                src_r, src_c = mapping[i]
                dst_r, dst_c = mapping[(i + k) % len(mapping)]
                ret[dst_r][dst_c] = grid[src_r][src_c]

        iterations = min(m // 2, n // 2)
        for it in range(iterations):
            rotate(it, k)
        return ret
