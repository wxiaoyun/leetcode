# https://leetcode.com/problems/build-a-matrix-with-conditions

from typing import Dict, List, Optional, Set


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
      def topo_order(edges: List[List[int]]) -> Optional[Dict[int, int]]: # Dict[node, index]
        adj_list: Dict[int, Set[int]] = {}

        for i in range(1, k+1):
          adj_list[i] = set()

        for fr, to in edges:
          adj_list[fr].add(to)
        
        order = []
        visited = set()
        path = set()

        def dfs(n: int) -> bool:
          if n in path:
            return False # cycle
          if n in visited:
            return True
          
          visited.add(n)
          path.add(n)
          
          for to_nodes in adj_list[n]:
            if not dfs(to_nodes):
              return False
          
          path.remove(n)
          order.append(n)
          return True
        
        for n in adj_list.keys():
          if not dfs(n):
            return None
        
        return {n:i for i, n in enumerate(reversed(order))}

      rows = topo_order(rowConditions)
      if not rows:
        return []
      cols = topo_order(colConditions)
      if not cols:
        return []

      mat = [[0] * k for _ in range(k)]
      for n, i in rows.items():
        j = cols[n]
        mat[i][j] = n
      return mat