import heapq
from typing import List

# https://leetcode.com/problems/maximize-happiness-of-selected-children

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
      k_happy = [] # min heap to remove the least happy kids
      for h in happiness:
        heapq.heappush(k_happy, h)
        if len(k_happy) > k:
          heapq.heappop(k_happy)
      
      res = 0
      i = k
      while k_happy:
        i -= 1
        h = heapq.heappop(k_happy)
        res += max(0, h-i)
      return res
    
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