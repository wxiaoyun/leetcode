class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        res = 0

        for c in s:
          count += 1 if c == '(' else -1

          while count < 0:
            count += 1
            res += 1

        while count > 0:
          count += -1
          res += 1
        
        return res