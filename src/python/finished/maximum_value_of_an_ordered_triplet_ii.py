from typing import List

# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_cur, max_diff, best = 0, 0, -1
        for n in nums:
            best = max(best, max_diff * n)
            max_diff = max(max_diff, max_cur - n)
            max_cur = max(max_cur, n)
        return best
