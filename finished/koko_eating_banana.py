# https://leetcode.com/problems/koko-eating-bananas/
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_needed(k: int) -> int:
            total_time = 0

            for count in piles:
                total_time += (count-1) // k + 1
            
            return total_time

        
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            mid_speed = (max_speed - min_speed) // 2 + min_speed

            time_taken = time_needed(mid_speed)

            if time_taken <= h:
                max_speed = mid_speed
            else:
                min_speed = mid_speed + 1

        return min_speed
