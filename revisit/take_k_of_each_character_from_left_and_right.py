from collections import defaultdict

# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
      cnt = {'a': 0, "b": 0, "c": 0}
      for char in s:
        cnt[char] += 1
      for c in cnt.values():
        if c < k:
          return -1
      
      N = len(s)
      best = 0
      count = {'a': 0, "b": 0, "c": 0}
      l = 0
      for r in range(N):
        count[s[r]] += 1

        while l <= r and (cnt['a'] - count['a'] < k or cnt['b'] - count['b'] < k or cnt['c'] - count['c'] < k):
          count[s[l]] -= 1
          l += 1
        
        best = max(best, r - l + 1) 

      return N - best

    # # Memory exceeded
    # def takeCharacters(self, s: str, k: int) -> int:
    #     dp = {}
    #     def helper(l: int, r: int, a: int, b: int, c: int) -> int:
    #       if a >= k and b >= k and c >= k:
    #         return 0 

    #       if l > r:
    #         return float('inf')

    #       key = (l, r)
    #       if key in dp:
    #         return dp[key]

    #       al = 1 if s[l] == 'a' else 0
    #       bl = 1 if s[l] == 'b' else 0
    #       cl = 1 if s[l] == 'c' else 0
          
    #       best = 1 + helper(l+1, r, a + al, b + bl, c + cl)

    #       ar = 1 if s[r] == 'a' else 0
    #       br = 1 if s[r] == 'b' else 0
    #       cr = 1 if s[r] == 'c' else 0

    #       best = min(best, 1 + helper(
    #         l, r-1, a+ ar, b+br, c+cr 
    #       ))

    #       dp[key] = best
    #       return best
    #     res = helper(0, len(s)-1, 0, 0,0)
    #     return -1 if res == float('inf') else res