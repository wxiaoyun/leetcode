# https://leetcode.com/problems/magic-squares-in-grid/

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n_magic = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                nums = set(range(1, 10))
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        nums.discard(grid[ii][jj])

                if len(nums) != 0:
                    continue

                checks = []
                for ii in [i - 1, i, i + 1]:
                    checks.append(sum(grid[ii][j - 1 : j + 2]))

                for jj in [j - 1, j, j + 1]:
                    checks.append(sum(grid[i + di][jj] for di in [-1, 0, 1]))

                checks.append(
                    sum(
                        grid[ii][jj]
                        for ii, jj in [(i - 1, j - 1), (i, j), (i + 1, j + 1)]
                    )
                )
                checks.append(
                    sum(
                        grid[ii][jj]
                        for ii, jj in [(i - 1, j + 1), (i, j), (i + 1, j - 1)]
                    )
                )

                equal = True
                target = checks[0]
                for sm in checks:
                    if sm != target:
                        equal = False
                        break

                if equal:
                    n_magic += 1

        return n_magic


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        if min(R, C) < 3:
            return 0

        count = 0

        for r in range(R - 2):
            for c in range(C - 2):
                seen = set()
                sums = [0] * 8
                has_invalid_num = False
                for i in range(3):
                    if has_invalid_num:
                        break
                    for j in range(3):
                        cur = grid[r + i][c + j]
                        if not 0 < cur < 10:
                            has_invalid_num = True
                            break
                        seen.add(cur)
                        sums[i] += cur
                        sums[j + 3] += cur
                        if i == j:
                            sums[6] += cur
                        if i + j == 2:
                            sums[7] += cur

                # print(seen, sums)
                if len(seen) == 9 and all([s == 15 for s in sums]):
                    count += 1

        return count
