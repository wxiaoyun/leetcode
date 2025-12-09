from collections import Counter, defaultdict
from typing import List

# https://leetcode.com/problems/count-special-triplets/


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = int(1e9) + 7
        total_occurrence = Counter(nums)

        prefix_occurrence = defaultdict(int)
        ans = 0
        for n in nums:
            n2 = n * 2
            prev_n2 = prefix_occurrence[n2]
            post_n2 = total_occurrence[n2] - prev_n2
            if n2 == n:
                post_n2 -= 1

            ans = (ans + prev_n2 * post_n2) % MOD
            prefix_occurrence[n] += 1

        return ans
