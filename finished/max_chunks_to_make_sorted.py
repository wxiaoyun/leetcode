from collections import defaultdict
from typing import List

# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        missing = defaultdict(int)
        chunks = 0
        for i, n in enumerate(arr):
          missing[i] += 1
          if missing[i] == 0:
            del missing[i]

          missing[n] -= 1
          if missing[n] == 0:
            del missing[n]
          
          if len(missing) == 0:
            chunks += 1
        
        return chunks