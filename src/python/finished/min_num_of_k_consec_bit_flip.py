# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        steps = 0
        flips = 0
        q = deque()

        for i in range(len(nums)):
            n = nums[i]
            if i >= k:
                flipped = q.popleft()
                if flipped:
                    flips -= 1
            
            tmp = (flips + n)%2

            if tmp == 0:
                if i > len(nums) - k:
                    return -1
                steps += 1
                flips += 1
                q.append(True)
            else:
                q.append(False)

        return steps
