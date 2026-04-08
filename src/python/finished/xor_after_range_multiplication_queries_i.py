from typing import List

# https://leetcode.com/problems/xor-after-range-multiplication-queries-i


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        ans = 0
        for v in nums:
            ans ^= v
        return ans
