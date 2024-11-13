from typing import List

# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def lower_bound(low: int, high: int, target: int) -> int:
          while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
              low = mid + 1
            else:
              high = mid
          return low

        count = 0
        for j in range(1, n):
          lower_idx = lower_bound(0, j, lower - nums[j])
          upper_idx = lower_bound(0, j, upper - nums[j]+1)
          count += upper_idx - lower_idx 
        return count
