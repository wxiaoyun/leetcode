from typing import List

# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        ltotal, lzero = 0, 0
        rtotal, rzero = 0, 0

        for n in nums1:
            if n == 0:
                lzero += 1
            ltotal += n

        for n in nums2:
            if n == 0:
                rzero += 1
            rtotal += n

        lmin = ltotal + lzero
        rmin = rtotal + rzero

        if lmin < rmin and lzero == 0:
            return -1

        if rmin < lmin and rzero == 0:
            return -1

        return max(lmin, rmin)
