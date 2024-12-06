from typing import List

# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        total = 0
        for i in range(1, n+1):
          if i in banned:
            continue
          if i + total > maxSum:
            break
          total += i
          count += 1
        return count

