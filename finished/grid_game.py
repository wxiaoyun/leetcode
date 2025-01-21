from typing import List

# https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        R = 2
        C = len(grid[0])
        botPreSum = [0] # Sum[i] == arr[:i]
        topSufSum = [0] * (C + 1) # Sum[i] = arr[i:]

        for c in range(C):
            cc = C - 1 - c
            topSufSum[cc] = topSufSum[cc+1] + grid[0][cc]
            botPreSum.append(botPreSum[-1] + grid[1][c])
        
        p2best = float('inf')
        for c in range(C):
            cur_best = max(topSufSum[c+1], botPreSum[c])
            p2best = min(p2best, cur_best)

        return p2best