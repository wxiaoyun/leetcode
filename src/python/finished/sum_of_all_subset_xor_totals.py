from typing import List
import numpy as np


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # total 2^n number of subsets
        # each number will appear in 2^(n-1) number of subsets

        N = len(nums)
        arr = np.array(nums)
        res = np.bitwise_or.reduce(arr)
        return int(res << (N - 1))

    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)

        def compute(i: int, acum: int) -> int:
            if i >= N:
                return acum
            n = nums[i]
            return compute(i + 1, acum ^ n) + compute(i + 1, acum)

        return compute(0, 0)
