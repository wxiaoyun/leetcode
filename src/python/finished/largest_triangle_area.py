# https://leetcode.com/problems/largest-triangle-area/


from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(i: int, j: int, k: int) -> float:
            ix, iy = points[i]
            jx, jy = points[j]
            kx, ky = points[k]

            v_vector = ((jx - kx), (jy - ky))
            u_vector = ((ix - kx), (iy - ky))

            cross_product = abs(u_vector[0] * v_vector[1] - u_vector[1] * v_vector[0])
            return cross_product / 2

        n = len(points)
        largest = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    largest = max(largest, area(i, j, k))
        return largest
