# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
      dp = [0] * (n+1)
      
      # how to form a number A:
      # Find the largest number B such that B = A/k
      # Given B is formed with i steps, it takes i + 1 + (k-1) steps to form A
      # - i steps to produce B
      # - 1 step to copy B
      # - (k-1) steps to paste B (k-1) timest to get kB

      for i in range(1, n):
        i = i + 1 # 1 indexed
        for j in reversed(range(1, i//2+1)):
          if i != i // j * j:
            continue
          
          # j is the largest factor of i
          factor = i // j
          dp[i] = dp[j] + factor
          break
      
      return dp[-1]