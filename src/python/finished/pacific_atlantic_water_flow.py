from collections import deque
from typing import List

# https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])

        def flood_up(initial_cells: list) -> set:
            visited = set()
            q = deque(initial_cells)

            while q:
                r, c = q.popleft()
                h = heights[r][c]
                cell = (r, c)
                if cell in visited:
                    continue
                visited.add(cell)

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue

                    hh = heights[rr][cc]
                    if hh < h:
                        continue

                    q.append((rr, cc))

            return visited

        pacific_ocean_initial = []
        altantic_ocean_initial = []

        for r in range(R):
            pacific_ocean_initial.append((r, 0))
            altantic_ocean_initial.append((r, C - 1))

        for c in range(C):
            pacific_ocean_initial.append((0, c))
            altantic_ocean_initial.append((R - 1, c))

        pacific_ocean = flood_up(pacific_ocean_initial)
        altantic_ocean = flood_up(altantic_ocean_initial)

        flow_to_both = []
        for r in range(R):
            for c in range(C):
                cell = (r, c)
                if cell in pacific_ocean and cell in altantic_ocean:
                    flow_to_both.append(cell)
        return flow_to_both
