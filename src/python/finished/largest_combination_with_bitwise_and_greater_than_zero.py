from typing import List

# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32 # LSB to MSB

        def inc_count(n: int) -> None:
          i = 0
          for i in range(32):
            if not n:
              break
            
            if n % 2 == 1:
              count[i] += 1
            n //= 2
          
        for c in candidates:
          inc_count(c)
        
        return max(count)