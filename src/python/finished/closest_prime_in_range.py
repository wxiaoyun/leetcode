from ast import List
import math

# https://leetcode.com/problems/closest-prime-numbers-in-range

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        not_prime = [False] * (right + 1)
        not_prime[1] = True

        for n in range(2, math.floor(math.sqrt(right)) + 1):
            if not_prime[n]:
                continue
            
            cur = n + n
            while cur <= right:
                not_prime[cur] = True
                cur += n
        
        # print(list(enumerate(not_prime)))

        best = float('inf')
        pair = [-1, -1]
        l = None
        for r in range(left, right + 1):
            # print(l, r)
            if not_prime[r]:
                continue
            
            if not l:
                l = r
                continue

            # print("PRIME", r)
            
            if r - l < best:
                pair = [l, r]
                best = r - l
            l = r

        return pair