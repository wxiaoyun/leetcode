from typing import List

# https://leetcode.com/problems/minimum-score-of-triangulation-of-polygon/


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def compute(dp: dict, l: int, r: int) -> int:
            key = (l, r)
            if key in dp:
                return dp[key]

            if l + 2 > r:
                return 0

            lr_prod = values[l] * values[r]
            if l + 2 == r:
                return lr_prod * values[l + 1]

            best = float("inf")
            for m in range(l + 1, r):
                best = min(
                    best, lr_prod * values[m] + compute(dp, l, m) + compute(dp, m, r)
                )

            dp[key] = best
            return best

        return compute({}, 0, len(values) - 1)


# TLE
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def compute(values: List[int], dp: dict, mask: int) -> int:
            if mask in dp:
                return dp[mask]

            vertices = []
            for i in range(len(values)):
                is_free = (mask & (1 << i)) != 0
                if is_free:
                    vertices.append(i)

            if len(vertices) == 3:
                prod = 1
                for index in vertices:
                    prod *= values[index]
                dp[mask] = prod
                return prod

            score = float("inf")
            vlen = len(vertices)
            for i in range(vlen):
                local_score = 1
                local_score *= values[vertices[(i - 1) % vlen]]
                local_score *= values[vertices[i]]
                local_score *= values[vertices[(i + 1) % vlen]]

                new_mask = mask ^ (1 << vertices[i])
                score = min(score, local_score + compute(values, dp, new_mask))

            dp[mask] = score
            return score

        mask = (1 << len(values)) - 1
        return compute(values, {}, mask)
