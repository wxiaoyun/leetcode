from collections import deque
from typing import List

# https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])
        out = [[-1] *  C  for _ in range(R)]

        q = deque()
        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r, c))
            
        step = 0
        while q:
            llen = len(q)
            for _ in range(llen):
                r, c = q.popleft()

                if out[r][c] != -1:
                    continue
                out[r][c] = step

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C or out[rr][cc] != -1:
                        continue
                    q.append((rr, cc))
            
            step += 1

        return out