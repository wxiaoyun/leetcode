# https://leetcode.com/problems/score-after-flipping-matrix/

# import copy

# class Solution:
#     def matrixScore(self, grid: List[List[int]]) -> int:
#         cache = {}

#         def eval_matrix(grid: List[List[int]]) -> int:
#             k = str(grid)

#             if k in cache:
#                 return cache[k]
            
#             total = 0
#             for row in grid:
#                 temp = 0
#                 for v in row:
#                     temp*=2
#                     temp+=v
#                 total+=temp
            
#             cache[k] = total
#             return total

#         def flip_row(grid: List[List[int]], r: int) -> List[List[int]]:
#             g = copy.deepcopy(grid)
#             g[r] = [1 if v == 0 else 0 for v in g[r]]
#             return g
        
#         def flip_col(grid: List[List[int]], c: int) -> List[List[int]]:
#             g = copy.deepcopy(grid)
#             for i in range(len(grid)):
#                 g[i][c] = 1 if g[i][c] == 0 else 0
#             return g

#         def generate_state(grid: List[List[int]]) -> List[List[List[int]]]:
#             states = []

#             for i in range(len(grid)):
#                 flipped = flip_row(grid, i)
#                 k = str(flipped)
#                 if k in cache:
#                     continue
#                 states.append(flipped)
#             for i in range(len(grid[0])):
#                 flipped = flip_col(grid, i)
#                 k = str(flipped)
#                 if k in cache:
#                     continue
#                 states.append(flipped)
            
#             return states
        
#         def helper(grid: List[List[int]]):
#             eval_matrix(grid)

#             for s in generate_state(grid):
#                 helper(s)
        
#         helper(grid)

#         return max(cache.values())

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def eval_matrix(grid: List[List[int]]) -> int:
            total = 0
            for row in grid:
                temp = 0
                for v in row:
                    temp*=2
                    temp+=v
                total+=temp
            return total

        def flip_row(g: List[List[int]], r: int) -> List[List[int]]:
            g[r] = [1 if v == 0 else 0 for v in g[r]]
            return g
        
        def flip_col(g: List[List[int]], c: int) -> List[List[int]]:
            for i in range(len(grid)):
                g[i][c] = 1 if g[i][c] == 0 else 0
            return g

        n_rows = len(grid)
        for r in range(n_rows):
            if grid[r][0] != 1:
                flip_row(grid, r)
        
        for c in range(1, len(grid[0])):
            n_ones = 0
            for row in grid:
                if row[c] == 1:
                    n_ones+=1
            
            if n_ones < n_rows/2:
                flip_col(grid, c)
        
        return eval_matrix(grid)
