# https://leetcode.com/problems/patching-array/

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        limit, steps, i = 0, 0, 0

        while limit < n:
            if i < len(nums) and nums[i] <= limit + 1:
                # we have all numbers from 1 to limit
                # so we can use nums[i] and complement of limit (< limit) to form it
                limit += nums[i]
                i += 1
            else:
                # we add limit
                limit = limit * 2 + 1
                steps += 1
        
        return steps