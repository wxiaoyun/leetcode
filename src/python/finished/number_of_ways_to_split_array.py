from typing import List

# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        psum = [0]
        for n in nums:
          psum.append(psum[-1] + n)
        total = psum[-1]

        splits = 0
        for i in range(len(nums)-1):
          left = psum[i+1]
          right = total - psum[i+1]
          if left >= right:
            splits += 1
        return splits
