# https://leetcode.com/problems/magnetic-force-between-two-balls

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def verify(dist: int):
            tmp = m
            prev = -float('inf')

            for p in position:
                if (p-prev) >= dist:
                    tmp -= 1
                    prev = p
                    if tmp <= 0:
                        return True
            
            return False
        
        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = (hi+lo)//2
            if verify(mid):
                lo = mid+1
            else:
                hi = mid
        
        return lo if verify(lo) else lo-1