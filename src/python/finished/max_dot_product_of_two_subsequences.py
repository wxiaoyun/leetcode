from typing import List, Optional


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def compute(
            dp: dict, n1: List[int], n2: List[int], i: int, j: int
        ) -> Optional[int]:
            if i >= len(n1) or j >= len(n2):
                return None

            key = (i, j)
            if key in dp:
                return dp[key]

            best = n1[i] * n2[j]

            # take
            res = compute(dp, n1, n2, i + 1, j + 1)
            if res is not None:
                best = max(best, n1[i] * n2[j] + res)

            # skip i
            res = compute(dp, n1, n2, i + 1, j)
            if res is not None:
                best = max(best, res)

            # skip j
            res = compute(dp, n1, n2, i, j + 1)
            if res is not None:
                best = max(best, res)

            dp[key] = best
            return best

        return compute({}, nums1, nums2, 0, 0)
