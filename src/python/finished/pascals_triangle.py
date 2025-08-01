# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        while len(rows) < numRows:
            prev = rows[-1]
            L = len(prev) + 1
            new = [0] * L
            for i in range(L):
                new[i] += prev[i - 1] if i > 0 else 0
                new[i] += prev[i] if i < len(prev) else 0
            rows.append(new)

        return rows
