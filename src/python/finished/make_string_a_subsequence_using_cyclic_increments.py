# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for c2 in str2:
          while True:
            if i >= len(str1):
              return False
            c1 = str1[i]
            i += 1

            if c1 == c2:
              break
            
            c1_alt = (ord(c1) - ord('a') + 1) % 26
            c1_alt = chr(c1_alt + ord('a'))
            if c1_alt == c2:
              break
          
        return True

            