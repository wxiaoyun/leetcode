from collections import deque
from typing import Optional

# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited_original = set()
        cloned = {}  # Dict[<original_node>, <cloned_node>]

        q = deque([node])
        while q:
            n = q.popleft()

            if not n or n in visited_original:
                continue
            visited_original.add(n)

            cln = Node(n.val)
            cloned[n] = cln

            for nb in n.neighbors:
                q.append(nb)

        for org in visited_original:
            cln = cloned[org]

            for org_nb in org.neighbors:
                cln.neighbors.append(cloned[org_nb])

        return cloned[node] if node else None
