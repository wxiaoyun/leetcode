from typing import List

# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def search(target: int) -> int:
            # search for the left most number that is >= target
            l, r = 0, len(nums)
            ans = len(nums)
            while l < r:
                m = l + (r - l) // 2
                mval = nums[m]
                if mval < target:
                    l = m + 1
                else:
                    ans = m
                    r = m
            return ans

        l = search(target)
        r = search(target + 1)
        n_elems = max(0, r - l)
        return n_elems > len(nums) / 2
