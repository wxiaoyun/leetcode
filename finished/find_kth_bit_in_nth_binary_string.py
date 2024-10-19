# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

from typing import List, Optional

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # n | length:
        # 1 | 1
        # 2 | (1*2) +1 = 3
        # 3 | (3*2) +1 = 7
        # 4 | (7*2) +1 = 15
        # 5 | (15*2) +1 = 31
        # 6 | (31*2) +1 = 63
        # ...
        # n | Sum<of i from 0 to n-1>(2^i)

        # kth bit of S_n, where l is the length of Sn
        # Let mid = (l-1)/2 + 1
        # Case 1: k < mid:
        # - Same as kth bit of S_n-1
        # Case 2: k == mid:
        # - "1" by definition
        # Case 3: k > mid:
        # - invert of (2*mid - k)th bit of S_n-1

        # Post submission remark: Len calculation can be optimized with (1 << n) - 1
        memo_len: List[Optional[int]] = [None] * n
        memo_len[0] = 1
        def calc_len(n: int) -> int:
          if memo_len[n-1] != None:
            return memo_len[n-1]
          
          l = calc_len(n-1) * 2 +1
          memo_len[n-1] = l
          return l

        def helper(n: int, k: int) -> str:
          if n == 1:
            if k == 1:
              return "0"
            else:
              raise Exception("Invalid arguments: n == 1 yet k != 1", k)
          
          l = calc_len(n)
          mid = (l-1) // 2 + 1

          if k == mid:
            return "1"
          elif k < mid:
            return helper(n-1, k)
          else: #k > mid
            # "0111001 1 0110001"
            #              ^ 11th
            # "011 1 001"
            #        ^ 5th
            # "0 1 1"
            # "0"
            b = helper(n-1, 2*mid - k)
            return "1" if b == "0" else "0" # Invert

        return helper(n, k)


