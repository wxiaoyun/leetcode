from collections import defaultdict
from typing import List

# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        lookup = defaultdict(int)

        for i in range(N):
            for j in range(i + 1, N):
                a, b = nums[i], nums[j]
                lookup[a * b] += 1
        
        count = 0
        for _, pairs in lookup.items():
            n_choose_2 = pairs * (pairs - 1) // 2
            permuted = n_choose_2 * 2 * 2 * 2
            count += permuted
        return count