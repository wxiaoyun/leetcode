from typing import List

# https://leetcode.com/problems/minimum-common-value


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n and j < m:
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            if a < b:
                i += 1
            else:
                j += 1
        return -1
