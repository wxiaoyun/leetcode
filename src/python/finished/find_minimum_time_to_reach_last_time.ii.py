from typing import List
import heapq

# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R = len(moveTime)
        C = len(moveTime[0])
        visited = set()

        pq = [(0, True, 0, 0)]
        while pq:
            t, is_even, r, c = heapq.heappop(pq)

            key = (r, c, is_even)
            if key in visited:
                continue
            visited.add(key)

            if r == R - 1 and c == C - 1:
                return t

            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if min(rr, cc) < 0 or rr >= R or cc >= C:
                    continue

                next_t = max(moveTime[rr][cc], t) + (1 if is_even else 2)

                heapq.heappush(pq, (next_t, not is_even, rr, cc))

        return -1
