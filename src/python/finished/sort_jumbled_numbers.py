# https://leetcode.com/problems/sort-the-jumbled-numbers

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
      def mapped_val(num: int) -> int:
        first_iteration = True # if the number is 0, we need to run it at least once
        cur = num
        res = 0
        pwr = 0

        while cur or first_iteration:
          d = cur % 10
          md = mapping[d]
          res += (10**pwr) * md
          cur = cur // 10
          pwr += 1
          first_iteration = False
        return res
      
      pairs = [(mapped_val(n), n) for n in nums]
      pairs.sort(key=lambda x: x[0])
      return [n for _, n in pairs]
        