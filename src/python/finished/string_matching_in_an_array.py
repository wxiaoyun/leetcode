from typing import List

# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key = lambda w: len(w))
        N = len(words)

        res = []
        for i in range(N):
          cur = words[i]
          for j in range(i+1, N):
            if cur in words[j]:
              res.append(cur)
              break
        return res