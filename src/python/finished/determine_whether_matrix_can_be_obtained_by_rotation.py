from typing import List

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat: List[List[int]]):
            n = len(mat)

            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # reverse columns
            for i in range(n):
                for j in range(n // 2):
                    mat[i][j], mat[i][n - j - 1] = mat[i][n - j - 1], mat[i][j]

        n = len(mat)
        for rotation in range(4):
            next = False
            for r in range(n):
                if next:
                    continue
                for c in range(n):
                    if mat[r][c] != target[r][c]:
                        next = True
                        break

            if not next:
                return True
            rotate(mat)

        return False
