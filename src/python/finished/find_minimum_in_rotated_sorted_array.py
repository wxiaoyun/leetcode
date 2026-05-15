# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case 1: non-rotated, min is at the beginning

        # case 2: rotated, min is after the beginning
        # 3, 4, 5, 0, 1, 2
        # if an array is rotated, then everything before the min, is larger than everything after the min

        is_rotated = nums[0] > nums[-1]
        if not is_rotated or len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)
        ans = -1
        while l < r:
            m = l + (r - l) // 2
            # print()
            # print(l, m, r)
            # print(nums[l], nums[m])

            # invariant: l <= pivot < r

            if r - l <= 2:
                return min(nums[l:r])

            if nums[l] < nums[m]:
                # turning point is on our right
                # m <= pivot
                l = m
                # print("R")
            else:  # nums[l] > nums[m]
                # l <= pivot <= m
                ans = m
                r = m + 1
                # print("L")

        return ans


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # invariant: min element is always between nums[l] and nums[r]
        while l <= r:
            # if nums[l] is smaller than nums[r] then nums[l] must be the smallest element
            if nums[l] <= nums[r]:
                return nums[l]

            # otherwise, there is a cliff between nums[l] and nums[r]
            mid = (r - l) // 2 + l

            if nums[l] <= nums[mid]:
                # there is no cliff between l and mid
                l = mid + 1
            else:
                r = mid

        return False
