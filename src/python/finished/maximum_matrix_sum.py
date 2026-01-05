from typing import List

# https://leetcode.com/problems/maximum-matrix-sum/


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        lt_cnt = 0
        total, smallest = 0, float("inf")
        for row in matrix:
            for n in row:
                if n < 0:
                    lt_cnt += 1
                total += abs(n)
                smallest = min(smallest, abs(n))

        if lt_cnt % 2 == 0:
            return total
        return total - 2 * smallest


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        res = 0
        non_pos_cnt = 0
        smallest = float("inf")
        for row in matrix:
            for n in row:
                smallest = min(smallest, abs(n))
                if n > 0:
                    res += n
                    continue

                non_pos_cnt += 1
                res += -n

        if non_pos_cnt % 2 == 0:
            return res

        res -= 2 * smallest
        return res
