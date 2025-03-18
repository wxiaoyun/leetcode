from collections import deque
from typing import List

#  https://leetcode.com/problems/longest-nice-subarray


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        q = deque()
        best = 1
        cur = 0
        for n in nums:
            # cur & test should not overlap: == 0
            while q and (cur & n) != 0:
                left = q.popleft()
                cur = cur ^ left

            q.append(n)
            cur = cur ^ n
            best = max(best, len(q))

        return best
