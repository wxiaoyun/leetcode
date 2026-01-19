from typing import List

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])

        # rps[r][c] = sum(mat[r][:c])
        row_prefix_sum = []
        for row in mat:
            psum = [0]
            for v in row:
                psum.append(v + psum[-1])
            row_prefix_sum.append(psum)

        # cps[c][r] = sum(mat[:r][c])
        col_prefix_sum = []
        for j in range(m):
            psum = [0]
            for i in range(n):
                psum.append(mat[i][j] + psum[-1])
            col_prefix_sum.append(psum)

        cache = {}

        def square_area(i: int, j: int, l: int) -> int:
            if l <= 0:
                return 0
            if l == 1:
                return mat[i][j]

            key = (i, j, l)
            if key in cache:
                return cache[key]

            area = 0
            half_l = l // 2
            area += square_area(i, j, half_l)
            area += square_area(i + half_l, j, half_l)
            area += square_area(i, j + half_l, half_l)
            area += square_area(i + half_l, j + half_l, half_l)

            if l % 2 == 1:
                area += row_prefix_sum[i + l - 1][j + l] - row_prefix_sum[i + l - 1][j]
                area += col_prefix_sum[j + l - 1][i + l] - col_prefix_sum[j + l - 1][i]
                area -= mat[i + l - 1][j + l - 1]

            cache[key] = area
            return area

        def possible(target: int) -> bool:
            for i in range(n - target + 1):
                for j in range(m - target + 1):
                    if square_area(i, j, target) <= threshold:
                        return True

            return False

        l, r = 0, min(n, m) + 1
        ans = 0
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans
