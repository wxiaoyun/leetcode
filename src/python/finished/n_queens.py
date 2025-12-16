from typing import List

# https://leetcode.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(
            n: int,
            mat: List[List[bool]],
            i: int,
            row_check: List[bool],
            col_check: List[bool],
            d1_check: List[bool],
            d2_check: List[bool],
            q_cnt: int,
            output: List[List[str]],
        ):
            if i >= n * n:
                if q_cnt == n:
                    board = ["".join("Q" if ok else "." for ok in row) for row in mat]
                    output.append(board)
                return

            # skip
            solve(
                n, mat, i + 1, row_check, col_check, d1_check, d2_check, q_cnt, output
            )

            r = i // n
            c = i % n

            # take
            if row_check[r] or col_check[c]:
                return

            # r - c
            # (0, n - 1) -> -n + 1 -> + n - 1 -> 0
            # (0, 0) -> 0          -> n - 1
            # (n - 1, 0) -> n - 1 -> 2n - 2
            d1 = r - c + n - 1

            # r + c
            # (0, 0) -> 0
            # (0, n - 1) -> n - 1
            # (n - 1, n - 1) -> 2n - 2
            d2 = r + c

            if d1_check[d1] or d2_check[d2]:
                return

            row_check[r] = True
            col_check[c] = True
            d1_check[d1] = True
            d2_check[d2] = True
            mat[r][c] = True
            solve(
                n,
                mat,
                i + 1,
                row_check,
                col_check,
                d1_check,
                d2_check,
                q_cnt + 1,
                output,
            )
            row_check[r] = False
            col_check[c] = False
            d1_check[d1] = False
            d2_check[d2] = False
            mat[r][c] = False

        mat = [[False] * n for _ in range(n)]
        row_check = [False] * n
        col_check = [False] * n
        d1_check = [False] * (n * 2 - 1)
        d2_check = [False] * (n * 2 - 1)
        output = []
        solve(n, mat, 0, row_check, col_check, d1_check, d2_check, 0, output)
        return output
