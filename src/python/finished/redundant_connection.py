from typing import List

# https://leetcode.com/problems/redundant-connection/

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
    
    def same_set(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e = None

        uf = UF()
        for a, b in edges:
            if uf.same_set(a, b):
                e = [a, b]
                continue
            uf.union(a, b)
        return e