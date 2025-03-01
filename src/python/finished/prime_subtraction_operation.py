from math import sqrt
from typing import List

# https://leetcode.com/problems/prime-subtraction-operation

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        nmax = max(nums)
        is_prime = [True] * (nmax + 1)
        is_prime[1] = False
        for n in range(2, int(sqrt(nmax+1)) + 1):
          if not is_prime[n]:
            continue
          
          cur = n * 2
          while cur < nmax + 1:
            is_prime[cur] = False
            cur += n
        
        target = 1
        i = 0
        for n in nums:
          while True:
            if target > n:
              return False

            diff = n - target
            target += 1
            if is_prime[diff]: # is_prime[0] is True even though 0 is not a prime
              break

        return True