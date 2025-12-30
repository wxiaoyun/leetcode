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


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets)
        adj_list = defaultdict(list)
        for fr, to in tickets:
            adj_list[fr].append(to)
        use = defaultdict(int)

        def dfs(node: str, builder: List[str]) -> List[str]:
            for i, nb in enumerate(adj_list[node]):
                if i < use[node]:
                    continue
                use[node] += 1
                dfs(nb, builder)

            builder.append(node)
            return builder

        res = dfs("JFK", [])
        res.reverse()
        return res
