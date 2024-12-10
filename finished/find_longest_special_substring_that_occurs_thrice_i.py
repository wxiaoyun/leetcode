from typing import DefaultDict

# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution:
    def maximumLength(self, s: str) -> int:
      N = len(s)
      count = DefaultDict(int)

      for i in range(0, N):
        for j in range(i, N):
          if s[i] != s[j]:
            break
          count[s[i:j+1]] += 1
      
      best = -1
      for w, cnt in count.items():
        if cnt >= 3:
          best = max(best, len(w))
      return best