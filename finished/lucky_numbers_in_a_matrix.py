# https://leetcode.com/problems/lucky-numbers-in-a-matrix


from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(row) for row in matrix]
        max_col = [max([matrix[r][c] for r in range(len(matrix))]) for c in range(len(matrix[0]))]

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
                    res.append(matrix[i][j])
        return res
        