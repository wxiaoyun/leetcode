from typing import List

# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


class Solution:
    def check(self, nums: List[int]) -> bool:
        incs = 0
        prev = nums[-1]
        for n in nums:
            if prev > n:
                incs += 1
            if incs > 1:
                return False
            prev = n
        return True


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 2:
            return True

        first = nums[0]
        prev = nums[0]

        first_dec = True
        for n in nums[1:]:
            if n < prev:
                if not first_dec:
                    return False

                first_dec = False

            if not first_dec and n > first:
                return False

            prev = n

        return True
