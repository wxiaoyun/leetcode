from collections import deque
from typing import List

# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def union(self, a: int, b: int) -> None:
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
          return None
        
        ar = self.rank[ap]
        br = self.rank[bp]

        if ar < br:
            self.parent[ap] = bp
        elif ar > br:
            self.parent[bp] = ap
        else:
            self.parent[bp] = ap
            self.rank[ap] += 1

        return None
    
    def find(self, a: int) -> int:
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 0

        p = self.parent[a]
        if p == a:
            return p

        self.parent[a] = self.find(p)
        return self.parent[a]
    
    def parents(self):
        return set(self.parent.values())

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        uf = UF()
        adj_list = [[] for _ in range(n+1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            uf.union(a, b)
        
        BLUE = "B"
        RED = "R"
        def switch(c):
            return RED if c == BLUE else BLUE
        
        def longest_bipartite(node: int) -> int:
            # print("NODE", node)
            visited = {}
            q = deque([(node, BLUE)])
            steps = 0
            color = BLUE

            while q:
                llen = len(q)

                new_level = False
                color = switch(color)
                for _ in range(llen):
                    nd, c = q.popleft()

                    if nd in visited:
                        prev_color = visited[nd]
                        if prev_color != c:
                            return -1
                        continue
                    visited[nd] = c
                    new_level = True
                    # print(nd)
                    for nb in adj_list[nd]:
                        q.append((nb, color))
                
                if new_level:
                    steps += 1
            
            return steps
        
        best = {i: 0 for i in range(n+1)}
        for i in range(n):
            node = i+1
            res = longest_bipartite(node)
            if res < 0:
                return -1
            comp = uf.find(node)
            best[comp] = max(best[comp], res)

        return sum(best.values())
