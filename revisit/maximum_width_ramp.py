# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_min = [None] * N
        prefix_min[0] = 0

        for i in range(1, N):
          prefix_min[i] = prefix_min[i-1] if nums[prefix_min[i-1]] <= nums[i] else i
        
        result = -1
        for j in reversed(range(1, N)):
          n = nums[j]
          while prefix_min and nums[prefix_min[-1]] <= n:
            result = max(result, j-prefix_min[-1])
            prefix_min.pop()
        return result