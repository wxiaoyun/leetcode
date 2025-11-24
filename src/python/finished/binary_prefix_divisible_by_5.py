from typing import List

# https://leetcode.com/problems/binary-prefix-divisible-by-5/


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        cur = 0
        for i, n in enumerate(nums):
            cur = (cur << 1) + n
            cur = cur % 5
            ans[i] = cur == 0
        return ans