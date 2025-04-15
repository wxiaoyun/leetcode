from typing import List
import bisect

# https://leetcode.com/problems/count-good-triplets-in-an-array


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        ridx = {n: i for i, n in enumerate(nums1)}
        st = []
        total = 0
        for i, n in enumerate(nums2):
            i1 = ridx[n]  # index of n in nums1

            l = bisect.bisect_left(
                st, i1
            )  # number of elements with smaller index than n in nums1 so far
            r = (N - 1 - i1) - (
                len(st) - l
            )  # (Number of elements to the right of i1) - (number of elements with index less than n in nums2 (which should be removed))

            total += l * r
            bisect.insort(st, i1)

        return total


class Solution:
    # Time limit exceeded, O(n^2)
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        # suppose we have a black box function F(n)
        # F(n) = the set of elements to the left of n in BOTH nums1 and nums2
        #
        # Then, the answer would be Sum over i in range(N) {
        # Sum over j in F(i) { F(j) }
        # }

        ridx = {n: i for i, n in enumerate(nums1)}
        left_of = {}

        for i, n in enumerate(nums2):
            left = set()
            left2 = set(nums2[:i])

            i1 = ridx[n]
            for j in range(i1):
                nj = nums1[j]
                if nj in left2:
                    left.add(nj)

            left_of[n] = left

        counts = 0
        for z in range(N):
            for y in left_of[z]:
                counts += len(left_of[y])

        return counts
