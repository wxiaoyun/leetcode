# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

from typing import Dict, List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
      all_chars = list(source)
      all_chars.extend(list(target))
      all_chars.extend(original)
      all_chars.extend(changed)
      all_chars = set(all_chars)

      cost_map: Dict[str, Dict[str, int]] = {
        i:{
          j:float('inf') for j in all_chars
        } for i in all_chars 
      }

      for c in all_chars:
        cost_map[c][c] = 0
      for i in range(len(original)):
        cost_map[original[i]][changed[i]] = min(
          cost_map[original[i]][changed[i]],
          cost[i]
        )

      for k in all_chars:
        for i in all_chars:
          for j in all_chars:
            cost_map[i][j] = min(
              cost_map[i][j],
              cost_map[i][k]+cost_map[k][j]
            )

      total_cost = 0

      for i in range(len(source)):
        cst = cost_map[source[i]][target[i]]
        if cst == float('inf'):
          return -1
        total_cost += cst

      return total_cost