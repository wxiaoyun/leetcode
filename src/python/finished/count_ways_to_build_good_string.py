# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
      MOD = 10 ** 9 + 7
      dp = {}
      def compute(ln: int) -> int:
        if ln > high:
          return 0

        if ln in dp:
          return dp[ln]
        
        ways = 0

        if ln >= low:
          ways += 1

        # add zeros
        ways += compute(ln+zero)
        ways %= MOD
        
        ways += compute(ln+one)
        ways %= MOD

        dp[ln] = ways
        return ways
        
      return compute(0)