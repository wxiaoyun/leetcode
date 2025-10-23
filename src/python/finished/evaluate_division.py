from typing import Dict, List, Optional, Tuple
from collections import defaultdict, deque

# https://leetcode.com/problems/evaluate-division/


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        cache = {}

        def check_cache(a: str, b: str) -> Optional[float]:
            if (a, b) in cache:
                return cache[(a, b)]
            if (b, a) in cache:
                return 1 / cache[(b, a)]
            return None

        def store_cache(a: str, b: str, fac: float) -> None:
            cache[(a, b)] = fac
            cache[(b, a)] = 1 / fac
            return None

        adj_list: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        for i in range(len(values)):
            u, v = equations[i]
            div = values[i]
            adj_list[u].append((v, div))
            adj_list[v].append((u, 1 / div))

            store_cache(u, v, div)

        def eval(a: str, b: str) -> float:
            visited = set()
            q = deque([(a, 1)])
            while q:
                node, fac = q.popleft()

                if node in visited:
                    continue
                visited.add(node)

                if node == b and node in adj_list and len(adj_list[node]):
                    store_cache(a, b, fac)
                    return fac

                if check_cache(node, b) is not None:
                    res = fac * check_cache(node, b)
                    store_cache(a, b, res)
                    return res

                for nbr, div in adj_list[node]:
                    q.append((nbr, fac * div))

            return -1

        return [eval(a, b) for a, b in queries]
