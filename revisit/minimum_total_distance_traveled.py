from typing import Dict, List, Tuple

# https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        dp: Dict[Tuple[int, int, int], int] = {}
        def helper(r: int, f: int, ff: int) -> int:
          key = (r, f, ff)
          if key in dp:
            return dp[key]

          if r >= len(robot):
            return 0
          
          if f >= len(factory):
            return float('inf')
          
          if ff >= factory[f][1]:
            return helper(r, f+1, 0)
          
          take = abs(robot[r] - factory[f][0]) + helper(r+1, f, ff+1)
          no_take = helper(r, f, ff+1)
          
          res = min(take, no_take)
          dp[key] = res
          return res

        return helper(0, 0, 0)