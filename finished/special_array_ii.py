from typing import List

# https://leetcode.com/problems/special-array-ii/

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        phase = 0
        tmp = [0] * N

        for i in range(1, N):
          if (nums[i] - nums[i-1]) % 2 == 0:
            phase += 1
          tmp[i] = phase
        # print(tmp)

        res = []
        for i, j in queries:
          res.append(True if tmp[i] == tmp[j] else False)
        return res