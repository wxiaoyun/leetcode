# https://leetcode.com/problems/sort-matrix-by-diagonals/


from typing import List, Tuple


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # -1: 0,1 1,2
        # 0: 0,0 1,1 2,2
        # 1: 1,0 2,1

        R = len(grid)
        C = len(grid[0])

        def get_coord(d: int, pos: int) -> Tuple[int, int]:
            r, c = pos, pos
            if d >= 0:
                r += d
            else:
                c -= d
            return r, c

        def partition(d: int, p: int, l: int, r: int) -> int:
            if r - l <= 1:
                return -1

            rp, cp = get_coord(d, p)
            pivot = grid[rp][cp]

            rr, cr = get_coord(d, r - 1)
            grid[rr][cr], grid[rp][cp] = grid[rp][cp], grid[rr][cr]

            k = l
            for i in range(l, r - 1):
                ri, ci = get_coord(d, i)
                if grid[ri][ci] >= pivot:
                    continue

                rk, ck = get_coord(d, k)
                grid[rk][ck], grid[ri][ci] = grid[ri][ci], grid[rk][ck]
                k += 1

            rk, ck = get_coord(d, k)
            grid[rr][cr], grid[rk][ck] = grid[rk][ck], grid[rr][cr]
            return k

        def sort(d: int, l: int, r: int) -> None:
            if r - l <= 1:
                return

            m = partition(d, l, l, r)
            sort(d, l, m)
            sort(d, m + 1, r)
            return None

        def rev(d: int, l: int, r: int) -> None:
            while l < r:
                rl, cl = get_coord(d, l)
                rr, cr = get_coord(d, r)

                grid[rl][cl], grid[rr][cr] = grid[rr][cr], grid[rl][cl]

                l += 1
                r -= 1
            return None

        for r in range(R):
            sort(r, 0, min(R - r, C))
            rev(r, 0, min(R - r, C) - 1)
        for c in range(1, C):
            sort(-c, 0, min(R, C - c))
        return grid
