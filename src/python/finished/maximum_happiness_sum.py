# https://leetcode.com/problems/maximize-happiness-of-selected-children/

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key=lambda h:-h)

        i = 0
        total_happiness = 0
        for h in happiness:
            total_happiness += max(0, h-i)
            i+=1
            if i == k:
                break
        return total_happiness    
