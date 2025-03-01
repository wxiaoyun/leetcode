from typing import List

# https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mb = 1 << maximumBit
        mask = mb - 1

        xor_sum = 0
        for n in nums:
          xor_sum ^= n
        
        
        n = len(nums)
        res = []

        for n in reversed(nums):
          rem = xor_sum % mb
          res.append(mask^rem)
          xor_sum ^= n
        
        return res

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mb = 1 << maximumBit
        mask = mb - 1

        xor_sum = 0
        for n in nums:
          xor_sum ^= n
        
        
        n = len(nums)
        res = []

        for n in reversed(nums):
          rem = xor_sum % mb

          comp = ['0'] * maximumBit
          tmp = list(bin(rem)[2:])
          comp[-len(tmp):] = tmp

          for i, c in enumerate(comp):
            comp[i] = '1' if c == '0' else '0'
          comp = int("".join(comp), 2)
          res.append(comp)

          xor_sum ^= n
        
        return res
