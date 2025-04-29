from typing import List

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        mx = max(nums)

        r = 0
        count = 0
        mx_count = 0
        for n in nums:
            while r < N and mx_count < k:
                if nums[r] == mx:
                    mx_count += 1
                r += 1

            if mx_count == k:
                count += N - r + 1

            if n == mx:
                mx_count -= 1

        return count
