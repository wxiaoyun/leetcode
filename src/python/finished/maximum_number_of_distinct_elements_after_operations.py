from typing import List

# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        cnt = 0
        smallest = -k
        for n in nums:
            distinct_n = max(smallest, n - k)
            if distinct_n > n + k:
                continue

            smallest = distinct_n + 1
            cnt += 1

        return cnt
