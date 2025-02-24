from collections import defaultdict, deque
from typing import List, Optional

# https://leetcode.com/problems/most-profitable-path-in-a-tree

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N = len(edges) + 1

        adj_list = [[] for _ in range(N)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def find_bob_path(path: List[int], visited: set) -> Optional[List[int]]:
            n = path[-1]
            visited.add(n)

            if n == 0:
                return path
            
            for nb in adj_list[n]:
                if nb in visited:
                    continue

                path.append(nb)
                res = find_bob_path(path, visited)
                if res:
                    return path
                path.pop()
            
            return None


        bpath = find_bob_path([bob], set())
        btime = defaultdict(lambda: float("inf"))
        for i, n in enumerate(bpath):
            btime[n] = i

        # print(bpath)

        best = -float('inf')
        q = deque([(0, 0)])
        visited = set()
        lvl = 0
        while q:
            qlen = len(q)

            for _ in range(qlen):
                m, na = q.popleft()
                visited.add(na)

                bt = btime[na]
                if bt < lvl: # bob arrives first
                    m += 0
                elif bt == lvl: # arrives at the same time
                    m += amount[na] // 2
                else: # bob arrives later/never
                    m += amount[na]

                nbs = adj_list[na]
                if len(nbs) == 1 and nbs[0] in visited: # leaf node
                    best = max(best, m)
                
                for nbr in nbs:
                    if nbr in visited:
                        continue
                    q.append((m, nbr))
            
            lvl += 1
        
        return best