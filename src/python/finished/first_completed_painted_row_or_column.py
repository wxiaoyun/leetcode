from typing import List

# https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        rows = [0] * R
        cols = [0] * C

        index = {}
        for r in range(R):
            for c in range(C):
                n = mat[r][c]
                index[n] = (r, c)
        
        for i, n in enumerate(arr):
            r, c = index[n]

            rows[r] += 1
            cols[c] += 1

            if rows[r] == C or cols[c] == R:
                return i
        
        return -1