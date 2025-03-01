# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
      # 100001

      flips = 0
      cur = ""
      count = 0

      for c in s:
        if c == cur:
          count += 1
          continue
        
        if count % 2 == 0:
          cur = c
          count = 1
          continue
        
        flips += 1
        cur = c
        count = 0
        
      return flips

        