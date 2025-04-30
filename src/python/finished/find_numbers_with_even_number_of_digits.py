from typing import List

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            cur = n
            digits = 0
            while cur != 0:
                cur //= 10
                digits += 1
            count += (digits + 1) % 2

        return count
