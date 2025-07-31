from typing import List

# https://leetcode.com/problems/bitwise-ors-of-subarrays/


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        orrs = set()
        ret = set()
        for cur in arr:
            orrs = set((n | cur) for n in orrs)
            orrs.add(cur)
            for n in orrs:
                ret.add(n)
        return len(ret)
