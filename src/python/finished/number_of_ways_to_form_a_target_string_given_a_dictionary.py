from typing import List

# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        N = len(target)
        W = len(words)
        WL = len(words[0])
        MOD = 10**9 + 7

        avail = [None] * WL
        for i in range(WL):
          occurances = {}
          for k in range(W):
            ch = words[k][i]
            if ch not in occurances:
              occurances[ch] = 0
            occurances[ch] += 1 # we tabulate the occurance of ch across words[k][i]
          avail[i] = occurances
        
        dp = {}
        def compute(i: int, k: int) -> int:
          if i >= N:
            return 1 # we have already formed 'target'
          
          if k >= WL:
            return 0 # we ran out of characters to form 'target'
          
          key = (i, k)
          if key in dp:
            return dp[key]
          
          next_ch = target[i]
          occurances = avail[k]
          ways = 0

          # skip
          ways += compute(i, k + 1)
          ways %= MOD

          # take
          if next_ch in occurances:
            occurance = occurances[next_ch]
            ways += (occurance * compute(i+1, k+1))
            ways %= MOD

          dp[key] = ways
          return ways

        return compute(0, 0)
          
