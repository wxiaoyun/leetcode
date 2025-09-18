from typing import List

# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        psum = [0]
        for _, a in fruits:
            psum.append(psum[-1] + a)

        def possible(startPos: int, k: int, l: int, r: int) -> bool:
            left_first = abs(startPos - l) + abs(r - l)
            right_first = abs(startPos - r) + abs(r - l)
            return min(left_first, right_first) <= k

        l, r = 0, 0
        best = 0
        while r < len(fruits):
            while r < len(fruits) and not possible(
                startPos, k, fruits[l][0], fruits[r][0]
            ):
                l += 1
                r = max(r, l)
            if r < len(fruits):
                best = max(best, psum[r + 1] - psum[l])
            r += 1
        return best
