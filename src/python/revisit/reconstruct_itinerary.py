from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/reconstruct-itinerary


# O(ElogE + V), Hierholzer's algorithm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets)
        adj_list = defaultdict(deque)
        for fr, to in tickets:
            adj_list[fr].append(to)

        def compute(node: str, out: List[str]):
            nbr_list = adj_list[node]
            while nbr_list:
                compute(nbr_list.popleft(), out)
            out.append(node)

        out = []
        compute("JFK", out)
        out.reverse()
        return out
