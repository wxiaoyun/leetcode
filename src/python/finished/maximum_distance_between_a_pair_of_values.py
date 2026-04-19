from typing import List

# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        best = 0
        for i, n in enumerate(nums1):
            if i >= len(nums2):
                break

            l, r = i, len(nums2)
            while l < r:
                j = l + (r - l) // 2
                mid = nums2[j]

                if n <= mid:
                    best = max(best, j - i)
                    l = j + 1
                else:
                    r = j

        return best
