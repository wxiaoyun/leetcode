# https://leetcode.com/problems/sort-array-by-increasing-frequency

from collections import Counter
from functools import cmp_to_key
from typing import List, Tuple


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
      cnt = Counter(nums)
      cnt = list(cnt.items())
      def cmpr(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        a_num, a_freq = a
        b_num, b_freq = b
        if a_freq == b_freq:
          return b_num - a_num
        else:
          return a_freq - b_freq
      cnt.sort(key=cmp_to_key(cmpr))
      res = []
      for num, freq in cnt:
        res.extend([num] * freq)
      return res
        