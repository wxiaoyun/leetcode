from typing import Dict, List, Tuple

# https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
      robot.sort()
      factory.sort()
      R = len(robot)
      F = len(factory)

      dp = {}
      def helper(r: int, f: int, fcnt: int) -> int:
        if r >= R:
          return 0
        
        if f >= F:
          return float('inf')
        
        if fcnt >= factory[f][1]:
          return helper(r, f+1, 0)
        
        key = (r, f, fcnt)
        if key in dp:
          return dp[key]
        
        rpos = robot[r]
        fpos = factory[f][0]

        # Fix at current factory
        best = abs(rpos-fpos) + helper(r+1, f, fcnt+1)

        # Skip current factory
        best = min(best, helper(r, f, fcnt+1))

        dp[key] = best
        return best
      
      return helper(0, 0, 0)
    
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
                return float("inf")

            if ff >= factory[f][1]:
                return helper(r, f + 1, 0)

            take = abs(robot[r] - factory[f][0]) + helper(r + 1, f, ff + 1)
            no_take = helper(r, f, ff + 1)

            res = min(take, no_take)
            dp[key] = res
            return res

        return helper(0, 0, 0)
