# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)

        seen = set()
        def helper(i: int, count: int) -> int:
          if i >= N:
            return count
          
          best = 0
          for j in range(i, N):
            k = j+1
            substr = s[i:k]

            if substr not in seen:
              seen.add(substr)
              best = max(best, helper(k, count+1))
              seen.remove(substr)
          return best
        
        return helper(0, 0)