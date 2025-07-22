# https://leetcode.com/problems/maximum-erasure-value/


from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        best = 0
        l = 0
        cur = 0
        for n in nums:
            while n in unique:
                lnum = nums[l]
                cur -= lnum
                unique.remove(lnum)
                l += 1

            cur += n
            unique.add(n)
            best = max(best, cur)

        return best
