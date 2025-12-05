from typing import List

# https://leetcode.com/problems/count-partitions-with-even-sum-difference/


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        cur = 0
        for n in range(len(nums) - 1):
            cur += n
            if (total - cur * 2) % 2 == 0:
                count += 1
        return count