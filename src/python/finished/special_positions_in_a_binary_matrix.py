from typing import List

# https://leetcode.com/problems/special-positions-in-a-binary-matrix


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        row_cnt = [0] * R
        col_cnt = [0] * C

        for r in range(R):
            for c in range(C):
                if mat[r][c] != 1:
                    continue
                row_cnt[r] += 1
                col_cnt[c] += 1

        specials = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1 and row_cnt[r] == 1 and col_cnt[c] == 1:
                    specials += 1
        return specials
