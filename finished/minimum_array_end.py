# https://leetcode.com/problems/minimum-array-end/

class Solution:
    def minEnd(self, n: int, x: int) -> int:
      x_bin = list(bin(x)[2:])
      ans = list(bin(n-1)[2:])

      res = []
      for c in reversed(x_bin):
        if c != '0':
          res.append('1')
          continue
        
        if ans:
          res.append(ans.pop())
        else:
          res.append('0')
      
      res.extend(reversed(ans))
      return int("".join(reversed(res)), 2)
