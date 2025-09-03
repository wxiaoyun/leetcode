# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # find pairs of points (xi, yi) and (xj, yj) such that
        #   no point (xk, yk) exists where k != i and k != j
        #   and xi <= xk <= xj and yj <= yk <= yi

        N = len(points)
        points = sorted(points, key=lambda p: (p[0], -p[1]))
        pairs = 0

        for i, (xi, yi) in enumerate(points):
            ymax = yi  # inclusive
            ymin = -float("inf")  # exclusive

            for j in range(i + 1, N):
                _, yj = points[j]

                if not (yj <= ymax and yj > ymin):
                    continue

                pairs += 1
                ymin = yj

        return pairs
