from typing import List

# https://leetcode.com/problems/count-subarrays-with-majority-element-i/


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0

        n = len(nums)
        for i in range(n):
            tcnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    tcnt += 1
                if tcnt > (j - i + 1) // 2:
                    count += 1
        return count
