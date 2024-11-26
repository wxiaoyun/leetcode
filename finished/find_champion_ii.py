from typing import List

# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        pcnt = {i: 0 for i in range(n)}
        for src, dst in edges:
          pcnt[dst] += 1
        
        champ = None
        for k, v in pcnt.items():
          if v == 0:
            if champ != None:
              return -1
            else:
              champ = k
        return champ if champ != None else -1