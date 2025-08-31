from typing import List

# https://leetcode.com/problems/sudoku-solver/


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_set = [[False] * 9 for _ in range(9)]
        col_set = [[False] * 9 for _ in range(9)]
        box_set = [[False] * 9 for _ in range(9)]

        for i in range(9 * 9):
            r = i // 9
            c = i % 9
            box = (r // 3 * 3) + (c // 3)

            n_str = board[r][c]
            if n_str == ".":
                continue
            # minus 1 to make n 0-indexed
            n = int(n_str) - 1

            row_set[r][n] = True
            col_set[c][n] = True
            box_set[box][n] = True

        def dfs(i: int = 0) -> bool:
            if i >= 9 * 9:
                return True

            r = i // 9
            c = i % 9
            box = (r // 3 * 3) + (c // 3)

            if board[r][c] != ".":
                return dfs(i + 1)

            for n in range(9):
                if row_set[r][n] or col_set[c][n] or box_set[box][n]:
                    continue

                board[r][c] = str(n + 1)
                row_set[r][n] = True
                col_set[c][n] = True
                box_set[box][n] = True
                if dfs(i + 1):
                    return True
                box_set[box][n] = False
                col_set[c][n] = False
                row_set[r][n] = False
                board[r][c] = "."

            return False

        dfs()
        return None
