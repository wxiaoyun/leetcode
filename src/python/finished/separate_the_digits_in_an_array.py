from typing import List

# https://leetcode.com/problems/separate-the-digits-in-an-array/


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for n in reversed(nums):
            cur = n
            while cur != 0:
                ans.append(cur % 10)
                cur //= 10
        ans.reverse()
        return ans
