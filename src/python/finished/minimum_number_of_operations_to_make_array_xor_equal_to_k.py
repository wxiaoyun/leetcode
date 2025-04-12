from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        diff = k
        for n in nums:
            diff ^= n

        b = str(bin(diff))[2:]
        return sum([int(d) for d in b])
