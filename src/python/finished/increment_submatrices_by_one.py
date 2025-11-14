from typing import List


# https://leetcode.com/problems/increment-submatrices-by-one/


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        deltas = [[] * n for _ in range(n)]
        for rs, cs, re, ce in queries:
            deltas[rs].append((re, cs, ce))

        mat = []
        for i, cur_row_deltas in enumerate(deltas):
            row_delta = [0] * (n + 1)
            for cur_row_delta in cur_row_deltas:
                re, cs, ce = cur_row_delta

                row_delta[cs] += 1
                row_delta[ce + 1] -= 1

                if i + 1 <= re:
                    deltas[i + 1].append(cur_row_delta)

            row = [0] * n
            cur = 0
            for i in range(n):
                cur += row_delta[i]
                row[i] = cur

            mat.append(row)

        return mat
