# https://leetcode.com/problems/minimum-increment-to-make-array-unique

from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        cur_min = -1
        for n in nums:
            if n <= cur_min:
                count += cur_min - n + 1
                cur_min += 1
            else:
                cur_min = n

        return count