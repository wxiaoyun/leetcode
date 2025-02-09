from collections import defaultdict
from typing import List

# https://leetcode.com/problems/count-number-of-bad-pairs

class Solution:
    # def countBadPairs(self, nums: List[int]) -> int:
    #     N = len(nums)

    #     c = 0
    #     for i in range(N):
    #         for j in range(i + 1, N):
    #             if j - i != nums[j] - nums[i]:
    #                 c += 1
    #     return 1

    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)

        buckets = defaultdict(int)
        for i, n in enumerate(nums):
            b = n - i
            buckets[b] += 1
        
        total_pairs = N * (N - 1) // 2
        bad_pairs = total_pairs
        for gd in buckets.values():
            good_pairs = gd * (gd - 1) // 2
            bad_pairs -= good_pairs
        return bad_pairs