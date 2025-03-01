# https://leetcode.com/problems/combination-sum-ii

from copy import copy
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      N = len(candidates)
      candidates.sort()

      res = []
      def helper(accum: int, i: int, arr: List[int]):
        if accum == target:
          res.append(arr)
          return

        if i >= N:
          return
        
        if accum > target:
          return
        
        # No take
        j = i + 1
        while j < N and candidates[j] == candidates[i]:
          j += 1
        if j < N:
          helper(accum, j, arr)
        
        # Take
        helper(accum+candidates[i], i+1, arr + [candidates[i]])
      
      helper(0, 0, [])
      return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      candidates.sort()
      output = []

      def generate(i: int, accum: List[int], _sum: int) -> None:
        if _sum > target:
          return
        
        if _sum == target:
          output.append(accum)
          return
        
        for j in range(i, len(candidates)):
          if j > i and candidates[j] == candidates[j-1]:
            continue
          generate(j+1, accum + [candidates[j]], _sum + candidates[j])
      
      generate(0, [], 0)
      return output

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      output = []

      def generate(i: int, accum: List[int], _sum: int) -> None:
        if _sum > target:
          return
        
        if _sum == target:
          output.add(tuple(sorted(accum)))
          return
        
        if i >= len(candidates):
          return

        # skip current num
        generate(i+1, accum, _sum)

        cp = copy.deepcopy(accum)
        cp.append(candidates[i])
        generate(i+1, cp, _sum+candidates[i])
      
      generate(0, [], 0)
      return list(output)
