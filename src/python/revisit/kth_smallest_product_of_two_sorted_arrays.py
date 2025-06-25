from typing import List
from bisect import bisect_left, bisect_right

# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays


class Solution:
    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))
        else:
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        mn1, mn2 = min(nums1), min(nums2)
        mx1, mx2 = max(nums1), max(nums2)
        boundary = [mn1, mn2, mx1, mx2]
        perm = []
        for i in range(len(boundary)):
            for j in range(i + 1, len(boundary)):
                perm.append(boundary[i] * boundary[j])

        left, right = min(perm), max(perm)
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
