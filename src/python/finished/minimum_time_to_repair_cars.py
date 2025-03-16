import math
from typing import List

# https://leetcode.com/problems/minimum-time-to-repair-cars


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def possible(max_time: int) -> bool:
            rem_cars = cars
            for r in ranks:
                # r * n^2 = t
                # n = sqrt(t / r)
                rem_cars -= math.floor(math.sqrt(max_time / r))

                if rem_cars <= 0:
                    return True
 
            return False
        
        # Small optimization: instead of the slowest mechanic, we put the fastest mechanic
        l, r = 0, min(ranks) * (cars ** 2) + 1

        while l < r:
            m = l + (r - l) // 2

            if possible(m):
                r = m
            else:
                l = m + 1
        
        return l

# DP solution: O(nk), TLE 
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        R = len(ranks)

        # What is the minimum time for r ... R-1 th mechanics to repair k remaining cars
        # dp[(r, k)] = min(for j in from 0 to k:
        #   max(time(j), dp[(r + 1, k - j)])
        # )   
        dp = {}

        def compute(i: int, rem: int) -> int:
            if rem <= 0:
                return 0
            if i >= R:
                return float('inf')
            
            key = (i, rem)
            if key in dp:
                return dp[key]

            r = ranks[i]
            best = float('inf')
            for n in range(rem + 1):
                best = min(
                    best,
                    max(
                        r * (n ** 2),
                        compute(i + 1, rem - n)
                    )
                )
            
            dp[key] = best
            return best

        return compute(0, cars)







