# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

from collections import defaultdict
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Suppose there is an edge from node u to node v
        # Then the ancestors of u is also the ancestors of v
        # So we only need to find the ancestors of the direct parent of each node

        parent_of = defaultdict(set)
        for fr, to in edges:
            parent_of[to].add(fr)

        ancestor_of = [None] * n
        def find_ancestor(node: int) -> List[int]:
            if ancestor_of[node] != None:
                return ancestor_of[node]
            
            parents = parent_of[node]
            tmp = set()
            for p in parents:
                tmp.add(p)
                tmp.update(find_ancestor(p))
            
            tmp = list(tmp)
            tmp.sort()
            ancestor_of[node] = tmp
            return tmp
        
        for i in range(n):
            find_ancestor(i)
        
        return ancestor_of