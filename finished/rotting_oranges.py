#  https://leetcode.com/problems/rotting-oranges/

from typing import List
import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rounds = 0
        draft = copy.deepcopy(grid)
  
        while (self.oneRoundOfRotting(grid, draft)):
            rounds+=1
        
        return rounds if self.hasAllRotten(grid) else -1
    

    # Carries out one round of rotting
    # returns true if some oranges has turned rotten, vice versa
    # copies the draft to reference at the end of each iteraiton
    def oneRoundOfRotting(self, reference: List[List[int]], new: List[List[int]]) -> bool:
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
                    if reference[r][c] == 2 and isValidMove(r+move[0],c+move[1]):
                        new[r+move[0]][c+move[1]] = 2 # spreads the rot
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