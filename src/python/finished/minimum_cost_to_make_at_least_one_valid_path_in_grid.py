from collections import defaultdict, deque
import heapq
from typing import List, Tuple


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def nxt(i: int, j: int, d: int) -> Tuple[int, int]:
            mp = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
            di, dj = mp[d]
            return i + di, j + dj

        R = len(grid)
        C = len(grid[0])
        dest = (R - 1, C - 1)

        adj_list = defaultdict(list)
        for r in range(R):
            for c in range(C):
                cur_d = grid[r][c]
                for d in range(1, 5):
                    rr, cc = nxt(r, c, d)

                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue

                    cost = 1 if d != cur_d else 0
                    adj_list[(r, c)].append((rr, cc, cost))

        # print(adj_list)

        visited = set()
        next_level = deque([(0, 0)])
        cur_cost = 0
        cur_level = deque()

        while next_level:
            tmp = cur_level
            cur_level = next_level
            next_level = tmp
            next_level.clear()

            while cur_level:
                node = cur_level.popleft()

                if node in visited:
                    continue
                visited.add(node)

                if node == dest:
                    return cur_cost

                for rr, cc, edge_cost in adj_list[node]:
                    nb = (rr, cc)
                    if edge_cost == 0:
                        cur_level.append(nb)
                    else:
                        next_level.append(nb)

            cur_cost += 1  # moving onto next level

        return -1

    def minCost(self, grid: List[List[int]]) -> int:
        def nxt(i: int, j: int, d: int) -> Tuple[int, int]:
            mp = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
            di, dj = mp[d]
            return i + di, j + dj

        R = len(grid)
        C = len(grid[0])
        dest = (R - 1, C - 1)

        adj_list = defaultdict(list)
        for r in range(R):
            for c in range(C):
                cur_d = grid[r][c]
                for d in range(1, 5):
                    rr, cc = nxt(r, c, d)

                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue

                    cost = 1 if d != cur_d else 0
                    adj_list[(r, c)].append((rr, cc, cost))

        # print(adj_list)

        visited = set()
        pq = [(0, 0, 0)]

        while pq:
            cost, r, c = heapq.heappop(pq)
            cost = cost
            node = (r, c)

            if node in visited:
                continue
            visited.add(node)

            if node == dest:
                return cost

            for rr, cc, edge_cost in adj_list[node]:
                heapq.heappush(pq, (cost + edge_cost, rr, cc))

        return -1
