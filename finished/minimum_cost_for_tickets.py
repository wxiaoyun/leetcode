from typing import List

# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        D = len(days)
        days = sorted(days)

        dp = {}
        def compute(idx: int) -> int:
          if idx >= D:
            return 0
          
          key = idx
          if key in dp:
            return dp[key]
          
          cost = float('inf')
          for i, d in enumerate([1, 7, 30]):
            covered_until = days[idx] + d
            j = idx
            while j < D and covered_until > days[j]:
              j += 1
            cost = min(cost, costs[i] + compute(j))
          
          dp[key] = cost
          return cost
        
        return compute(0)
