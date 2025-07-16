# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        alt_odd = 0
        alt_even = 0

        for n in nums:
            if n % 2 == 0:
                evens += 1
                alt_even = max(alt_even, alt_odd + 1)
            else:
                odds += 1
                alt_odd = max(alt_odd, alt_even + 1)

        return max(evens, odds, alt_odd, alt_even)
