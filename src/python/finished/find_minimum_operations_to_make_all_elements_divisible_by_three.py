import math
from collections import List

# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for n in nums:
            ops_needed = min(n - math.floor(n / 3) * 3, math.ceil(n / 3) * 3 - n)
            ops += ops_needed
        return ops
