from typing import List

# https://leetcode.com/problems/count-submatrices-with-all-ones/


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])

        ret = 0
        col_height = [0] * C
        for r in range(R):
            for c in range(C):
                col_height[c] = 0 if not mat[r][c] else col_height[c] + 1

            sm = []
            height_stack = []
            for c in range(C):
                while height_stack and col_height[height_stack[-1]] >= col_height[c]:
                    height_stack.pop()

                if height_stack:
                    mat_count = sm[height_stack[-1]]
                    mat_count += col_height[c] * (c - height_stack[-1])
                else:
                    mat_count = col_height[c] * (c + 1)

                ret += mat_count
                sm.append(mat_count)
                height_stack.append(c)

        return ret
