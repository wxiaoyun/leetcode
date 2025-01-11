from collections import Counter

# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)

        if k > N:
          return False
        
        if k == N:
          return True
        
        cnt = Counter(s)
        odds = 0
        for _, fq in cnt.items():
          if fq % 2 == 1:
            odds += 1
        
        if k < odds:
          return False
        
        return True