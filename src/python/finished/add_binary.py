# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a)
        blen = len(b)
        abmax = max(alen, blen)

        res = []
        carry = 0
        for i in range(abmax):
          tmp = carry

          if i < alen and a[alen - 1 - i] == '1':
            tmp += 1
          if i < blen and b[blen - 1 - i] == '1':
            tmp += 1

          if tmp > 1:
            tmp = tmp % 2
            carry = 1
          else:
            carry = 0
          
          res.append(str(tmp))
        
        if carry:
          res.append('1')
        
        return "".join(reversed(res))

            