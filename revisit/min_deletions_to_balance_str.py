# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

from typing import List


class Solution:
    def minimumDeletions(self, s: str) -> int:
        tmp = 0

        # prefix sum of number of 'b's
        prefix_sum: List[int] = []
        for i in range(len(s)):
          if s[i] == 'b':
            tmp += 1
          prefix_sum.append(tmp)

        tmp = 0

        # post fix sum of number of 'a's
        postfix_sum: List[int] = [None] * len(s)
        for j in reversed(range(len(s))):
          if s[j] == 'a':
            tmp += 1
          postfix_sum[j] = tmp

        _min = float('inf')
        for i in range(len(s)):
          _min = min(
            _min,
            (prefix_sum[i-1] if i > 0 else 0) + (postfix_sum[i+1] if i < len(s)-1 else 0)
          )

        return _min

# class Solution:
#     def minimumDeletions(self, s: str) -> int:
        # dp: Dict[Tuple[int, int], int] = {}

        # def shrink(l: int, r: int) -> Optional[Tuple[int, int]]:
        #   if l >= r:
        #     return None
          
        #   while l < r and s[l] == 'a':
        #     l += 1
          
        #   while l < r and s[r] == 'b':
        #     r -= 1
          
        #   # only return l, r if there is at least one 'ba'
        #   return None if l >= r or s[l] == s[r] else (l, r)
        
        # def balance(l: int, r: int) -> int:
        #   ret = shrink(l, r)

        #   if not ret:
        #     return 0
          
        #   nl, nr = ret          
          
        #   if (nl, nr) in dp:
        #     return dp[(nl, nr)]

        #   res = min(
        #     1+balance(nl+1, nr), # remove left most 'b'
        #     1+balance(nl, nr-1) # remove right most 'a
        #   )
        #   dp[(nl, nr)] = res
        #   return res

        # return balance(0, len(s)-1)