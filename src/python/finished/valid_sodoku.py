# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [[False] * 9 for _ in range(9)]
        col_set = [[False] * 9 for _ in range(9)]
        box_set = [[False] * 9 for _ in range(9)]

        R = len(board)
        C = len(board[0])
        for i in range(R):
            for j in range(C):
                n_str = board[i][j]
                if n_str == ".":
                    continue
                n = int(n_str) - 1

                if row_set[i][n]:
                    return False
                row_set[i][n] = True

                if col_set[j][n]:
                    return False
                col_set[j][n] = True

                box_r = i // 3
                box_c = j // 3
                box_idx = box_r * 3 + box_c
                if box_set[box_idx][n]:
                    return False
                box_set[box_idx][n] = True

        return True
