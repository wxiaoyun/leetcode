# https://leetcode.com/problems/diagonal-traverse/

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0,0
        # 0,1
        # 1,0
        # 2,0
        # 1,1
        # 0,2

        R = len(mat)
        C = len(mat[0])

        UP = (-1, 1)
        DN = (1, -1)
        direction = UP

        ret = [-1] * (R * C)
        cur = (0, 0)
        for i in range(R * C):
            r, c = cur
            ret[i] = mat[r][c]

            dr, dc = direction
            rr = r + dr
            cc = c + dc

            if min(rr, cc) < 0 or rr >= R or cc >= C:
                if direction == UP:
                    direction = DN
                    if cc < C:
                        rr, cc = (r, cc)
                    else:
                        rr, cc = (r + 1, c)
                else:
                    direction = UP
                    if rr < R:
                        rr, cc = (rr, c)
                    else:
                        rr, cc = (r, c + 1)

            cur = (rr, cc)

        return ret
