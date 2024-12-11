from typing import List

# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        rangee =  2 * k
        best = 0
        l = 0
        for r in range(len(nums)):
          while nums[r] - nums[l] > rangee:
            l += 1
          best = max(best, r - l + 1)
        return best