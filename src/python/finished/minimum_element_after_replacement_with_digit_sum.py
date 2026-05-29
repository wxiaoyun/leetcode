from typing import List

# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(d) for d in str(n)) for n in nums)
