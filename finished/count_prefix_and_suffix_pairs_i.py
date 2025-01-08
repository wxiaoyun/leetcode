from typing import List

# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        word_idx = sorted(
          [(w, i) for i, w in enumerate(words)], 
          key = lambda x: len(x[0])
        )
        N = len(word_idx)

        count = 0
        for i in range(N):
          a, ai = word_idx[i]
          alen = len(a)
          for j in range(i+1, N):
            b, bi = word_idx[j]

            if ai > bi:
              continue
            
            if b[:alen] == a and b[-alen:] == a:
              count += 1

        return count