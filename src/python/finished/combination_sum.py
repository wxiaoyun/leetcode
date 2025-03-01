from typing import List

# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []

        def helper(accum: int, i: int, arr: List[int]):
          if accum == target:
            res.append(arr)
            return
          if accum > target or i >= N:
            return

          helper(accum + candidates[i], i, arr + [candidates[i]])
          helper(accum, i + 1, arr)
      
        helper(0, 0, [])
        return res