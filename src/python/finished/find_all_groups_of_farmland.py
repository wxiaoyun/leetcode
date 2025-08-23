from typing import List, Tuple

# https://leetcode.com/problems/find-all-groups-of-farmland


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def tmax(ar: int, ac: int, br: int, bc: int) -> Tuple[int, int]:
            if ar > br or ac > bc:
                return (ar, ac)
            return (br, bc)

        def tmin(ar: int, ac: int, br: int, bc: int) -> Tuple[int, int]:
            if ar < br or ac < bc:
                return (ar, ac)
            return (br, bc)

        R = len(land)
        C = len(land[0])

        def flood_find(
            grid: List[List[int]], r: int, c: int
        ) -> Tuple[int, int, int, int]:
            if grid[r][c] <= 0:
                return (R, C, -1, -1)
            grid[r][c] = -1

            ar, ac, br, bc = r, c, r, c
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue

                cr, cd, dr, dd = flood_find(grid, rr, cc)
                ar, ac = tmin(ar, ac, cr, cd)
                br, bc = tmax(br, bc, dr, dd)
            return (ar, ac, br, bc)

        res = []
        for r in range(R):
            for c in range(C):
                if land[r][c] <= 0:
                    continue
                res.append(flood_find(land, r, c))
        return res
