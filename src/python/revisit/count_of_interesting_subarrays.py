from collections import defaultdict
from typing import List

# https://leetcode.com/problems/count-of-interesting-subarrays


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)

        count = 0
        deez = defaultdict(int)
        deez[0] = 1
        prefix = 0
        for i in range(N):
            prefix = (prefix + (1 if nums[i] % modulo == k else 0)) % modulo
            target = (prefix - k) % modulo

            count += deez[target]
            deez[prefix] += 1

        return count
