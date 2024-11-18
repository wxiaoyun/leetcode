from typing import List

# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        rev = False
        if k < 0:
          code.reverse()
          rev = True
          k = -k

        n = len(code)

        if k == 0:
          return [0] * n

        psum = [0]
        for c in code:
          psum.append(psum[-1] + c)
        
        res = [0] * n
        for i in range(n):
          res[i] += psum[min(i+k+1, n)] - psum[i+1]
          res[i] += psum[max(i+k+1-n, 0)]
        
        if rev:
          res.reverse()

        return res