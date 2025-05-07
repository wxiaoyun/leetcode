import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R = len(moveTime)
        C = len(moveTime[0])
        visited = [[False] * C for _ in range(R)]

        pq = [(0, 0, 0)]
        while pq:
            t, r, c = heapq.heappop(pq)

            if visited[r][c]:
                continue
            visited[r][c] = True

            if r == R - 1 and c == C - 1:
                return t

            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue

                heapq.heappush(pq, (max(t, moveTime[rr][cc]) + 1, rr, cc))

        return -1
