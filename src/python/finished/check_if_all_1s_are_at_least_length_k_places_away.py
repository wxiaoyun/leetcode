from typing import List


# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_seen = -k - 1
        for i, n in enumerate(nums):
            if n != 1:
                continue

            # n == 1
            if i - last_seen <= k:
                return False
            last_seen = i
        return True
