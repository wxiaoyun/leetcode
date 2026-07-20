from typing import List

# https://leetcode.com/problems/shift-2d-grid/


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])

        rlen = k + 1
        ring_buffer = [-1] * rlen
        head = 0
        tail = 0
        for i in range(R * C + k):
            j = i % (R * C)
            r, c = j // C, j % C
            if i < R * C:
                ring_buffer[tail % rlen] = grid[r][c]
                tail += 1
            if i >= k:
                grid[r][c] = ring_buffer[head % rlen]
                head += 1

        return grid
