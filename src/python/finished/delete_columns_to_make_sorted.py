from typing import List

# https://leetcode.com/problems/delete-columns-to-make-sorted/


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        ndel = 0
        for j in range(m):
            for i in range(1, n):
                if strs[i - 1][j] > strs[i][j]:
                    ndel += 1
                    break
        return ndel
