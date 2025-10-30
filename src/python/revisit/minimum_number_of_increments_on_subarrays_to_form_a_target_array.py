from typing import List

# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/


class Solution:
    def minNumberOperations(self, target: List[int], base: int = 0) -> int:
        ops = target[0]
        for i in range(len(target) - 1):
            ops += max(0, target[i + 1] - target[i])
        return ops


# TLE: O(n^2)
class Solution:
    def minNumberOperations(self, target: List[int], base: int = 0) -> int:
        if not target:
            return 0
        ref = min(target)

        total_ops = ref - base
        l = 0
        while l < len(target):
            while l < len(target) and target[l] == ref:
                l += 1

            r = l
            while r < len(target) and target[r] > ref:
                r += 1
            total_ops += self.minNumberOperations(target[l:r], ref)

            l = r
        return total_ops
