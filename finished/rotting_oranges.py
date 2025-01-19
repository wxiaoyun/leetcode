#  https://leetcode.com/problems/rotting-oranges/

from typing import List
import copy


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        empty = 0
        fresh = 1
        rotten = 2
        steps = 0
        cur_level = set()
        next_level = set()
        visited = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == rotten:
                    next_level.add((r, c))

        while next_level:
            tmp = cur_level
            cur_level = next_level
            next_level = tmp
            next_level.clear()

            cur_level_occupied = False
            for cell in cur_level:
                if cell in visited:
                    continue
                visited.add(cell)
                cur_level_occupied = True

                r, c = cell
                grid[r][c] = rotten

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= R or cc >= C:
                        continue

                    if grid[rr][cc] != fresh:
                        continue

                    if (rr, cc) not in visited and (rr, cc) not in cur_level:
                        next_level.add((rr, cc))

            if cur_level_occupied and next_level:
                steps += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == fresh:
                    return -1

        return steps

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rounds = 0
        draft = copy.deepcopy(grid)

        while self.oneRoundOfRotting(grid, draft):
            rounds += 1

        return rounds if self.hasAllRotten(grid) else -1

    # Carries out one round of rotting
    # returns true if some oranges has turned rotten, vice versa
    # copies the draft to reference at the end of each iteraiton
    def oneRoundOfRotting(
        self, reference: List[List[int]], new: List[List[int]]
    ) -> bool:
        def isValidMove(r: int, c: int) -> bool:
            if r < 0 or c < 0:
                return False
            if r >= len(reference) or c >= len(reference[r]):
                return False
            # the grid is fresh orange
            return reference[r][c] == 1

        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        hasChanged = False
        for r in range(len(reference)):
            for c in range(len(reference[r])):
                for move in moves:
                    if reference[r][c] == 2 and isValidMove(r + move[0], c + move[1]):
                        new[r + move[0]][c + move[1]] = 2  # spreads the rot
                        hasChanged = True

        # # Update the reference
        reference[:] = copy.deepcopy(new)

        return hasChanged

    # Checks if all oranges has rotten
    def hasAllRotten(self, grid: List[List[int]]) -> bool:
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:  # Found a fresh orange
                    return False
        return True
