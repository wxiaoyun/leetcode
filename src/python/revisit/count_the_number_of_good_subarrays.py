from collections import defaultdict
from typing import List

# https://leetcode.com/problems/count-the-number-of-good-subarrays


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        freq = defaultdict(int)

        r = 0
        pairs = 0
        subarrays = 0
        for l in range(N):
            while pairs < k and r < N:
                n = nums[r]

                f = freq[n]
                pairs -= f * (f - 1) // 2

                freq[n] += 1
                f = freq[n]
                pairs += f * (f - 1) // 2

                r += 1

            if pairs >= k:
                subarrays += N - r + 1

            n = nums[l]
            f = freq[n]
            pairs -= f * (f - 1) // 2

            freq[n] -= 1
            f = freq[n]
            pairs += f * (f - 1) // 2

        return subarrays
