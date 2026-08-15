from collections import Counter
from typing import List

# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        l = 0
        check = 0
        for k, v in cnt.items():
            l += v
            if v % 2 != 0:
                check ^= k

        if check == 0:
            if len(cnt) == 1 and cnt[0]:
                return 0
            return l - 1
        return l
