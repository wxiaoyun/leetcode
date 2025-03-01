from typing import List

# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        pcnt = {i: 0 for i in range(n)}
        for src, dst in edges:
          pcnt[dst] += 1
        
        champ = -1
        for k, v in pcnt.items():
          if v == 0:
            if champ >= 0:
              return -1
            else:
              champ = k
        return champ if champ >= 0 else -1