# https://leetcode.com/problems/find-missing-observations/

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
      m = len(rolls)
      npm = n + m
      total = npm * mean

      msum = sum(rolls)
      remaining = total - msum
      if remaining > 6 * n or remaining < 1 * n:
        return []

      navg = remaining / n
      navg_low = int(navg // 1)
      low_sum = navg_low * n
      n_missing = remaining - low_sum

      res = []
      for i in range(n-n_missing):
        res.append(navg_low)
      for i in range(n_missing):
        res.append(navg_low + 1)
      return res