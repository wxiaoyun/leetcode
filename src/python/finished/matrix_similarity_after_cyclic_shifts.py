from typing import List

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                c_shift = c + (-k if r % 2 == 0 else k)
                c_shift %= n

                if mat[r][c] != mat[r][c_shift]:
                    return False

        return True
