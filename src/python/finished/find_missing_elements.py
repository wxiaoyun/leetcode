from typing import List

# https://leetcode.com/problems/find-missing-elements/


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = [False] * 101
        lo, hi = 101, 0

        for n in nums:
            lo = min(lo, n)
            hi = max(hi, n)
            present[n] = True

        ans = []
        for i in range(lo + 1, hi):
            if not present[i]:
                ans.append(i)
        return ans
