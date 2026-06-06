from typing import List

# https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        for n in nums:
            left_sum.append(n + left_sum[-1])

        n = len(nums)
        ans = [0] * n
        right_sum = 0
        for j in reversed(range(n)):
            ans[j] = abs(left_sum[j] - right_sum)
            right_sum += nums[j]
        return ans
