# https://leetcode.com/problems/count-number-of-teams


from typing import Dict, List, Tuple


class Solution:
    def numTeams(self, rating: List[int]) -> int:
      def find_nums(i: int, delta: int) -> Tuple[int, int]:
        bigger, smaller = 0, 0

        j = i
        while j >= 0 and j < len(rating):
          if rating[j] > rating[i]:
            bigger += 1
          if rating[j] < rating[i]:
            smaller += 1
          j += delta
        
        return bigger, smaller
      
      result = 0
      for i in range(1, len(rating)-1):
        lb, ls = find_nums(i, -1)
        rb, rs = find_nums(i, 1)
        result += lb*rs + ls*rb
      return result
    
class Solution2:
    def numTeams(self, rating: List[int]) -> int:
      dp: Dict[Tuple[bool, int, int], int] = {}

      def count(i: int, inc: bool, accum: int) -> int:
        key = (inc, i, accum)
        if key in dp:
          return dp[key]

        if accum == 3:
          return 1
        
        if i >= len(rating):
          return 0
        
        result = 0

        for j in range(i+1, len(rating)):
          if (inc and rating[j] > rating[i]):
            result += count(j, inc, accum+1)
          if (not inc and rating[j] < rating[i]):
            result += count(j, inc, accum+1)

        dp[key] = result
        return result

      return sum([
        count(i, True, 1) + count(i, False, 1) for i in range(len(rating)-2)
      ]) 