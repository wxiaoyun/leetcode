# https://leetcode.com/problems/spiral-matrix-iii/

from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_valid_coord(r: int, c: int) -> bool:
            if min(r, c) < 0 or r >= rows or c >= cols:
                return False
            return True
        
        path = []
        dir = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        count = 0
        dir_idx = 0
        step = 1
        cur_coord = (rStart, cStart)

        while count < rows * cols:
            for _ in range(2):
                dx, dy = dir[dir_idx%4]

                for i in range(1, step+1):
                    cur_r, cur_c = cur_coord
                    if is_valid_coord(cur_r, cur_c):
                        path.append(cur_coord)
                        count += 1

                    r = cur_r + dx
                    c = cur_c + dy
                    cur_coord = (r, c)
                
                dir_idx += 1
            step += 1
            

        return path