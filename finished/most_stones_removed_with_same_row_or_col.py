# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from collections import defaultdict
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
      row_stones = defaultdict(list) # Dict[row, list of stones]
      col_stones = defaultdict(list) # Dict[col, list of stones]
      for r, c in stones:
        row_stones[r].append(c)
        col_stones[c].append(r)

      visited = set()

      def flood(r: int, c: int) -> None:
        if (r, c) in visited:
          return None
        visited.add((r, c))

        for cc in row_stones[r]:
          flood(r, cc)
        for rr in col_stones[c]:
          flood(rr, c)   
      
      stones_kept = 0
      for r, c in stones:
        if (r, c) in visited:
          continue
        flood(r, c)
        stones_kept += 1
      return len(stones) - stones_kept

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r, c in stones:
            rows[r].add((r, c))
            cols[c].add((r, c))

        visited = set()

        def flood(r: int, c: int) -> None:
            if (r, c) in visited:
                return None

            visited.add((r, c))
            for rr, cc in rows[r]:
                flood(rr, cc)
            for rr, cc in cols[c]:
                flood(rr, cc)

        islands = 0
        for r, c in stones:
            if (r, c) in visited:
                continue
            islands += 1
            flood(r, c)

        return len(stones) - islands

# Attempt 1: TLE
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         rows = defaultdict(set)
#         cols = defaultdict(set)
#         remaining = set()

#         for r, c in stones:
#           rows[r].add((r, c))
#           cols[c].add((r, c))
#           remaining.add((r, c))

#         cache = {}
#         most_stones = -1
#         # dfs
#         def dfs() -> int:
#           if len(remaining) == 0:
#             return 0

#           key = frozenset(remaining)
#           if key in cache:
#             return cache[key]

#           res = 0 # by default if no row or col has 2 element, we remove 0 stones
#           for r, c in remaining:
#             if len(rows[r]) > 1 or len(cols[c]) > 1:
#               rows[r].remove((r, c))
#               cols[c].remove((r, c))
#               remaining.remove((r, c))
#               res = max(res, 1 + dfs())
#               rows[r].add((r, c))
#               cols[c].add((r, c))
#               remaining.add((r, c))

#           cache[key] = res
#           return res

#         return dfs()
