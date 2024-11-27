from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for i in range(n-1):
          adj_list[i].append(i+1)
        
        def bfs(adj_list) -> int:
          q = deque([0])
          visited = set()
          dist = 0

          while q:
            l = len(q)
            for _ in range(l):
              c = q.popleft()

              if c in visited:
                continue
              visited.add(c)

              if c == n-1:
                return dist

              for ngb in adj_list[c]:
                q.append(ngb)

            dist += 1
          return -1
        
        ans = []
        for u, v in queries:
          adj_list[u].append(v)
          ans.append(bfs(adj_list))
        return ans


