from collections import deque
from copy import copy
from typing import List

# https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        final_state = str([
          [1, 2, 3],
          [4, 5, 0]
        ])

        def get_neighbours(i: int, j: int) -> List[List[int]]:
          out = []
          for y, x in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if min(y, x) < 0 or y > 1 or x > 2:
              continue
            out.append((y, x))
          return out
        
        q = deque()
        for i, row in enumerate(board):
          for j, n in enumerate(row):
            if n == 0:
              q.append((board, i, j, 0))
        
        visited = set()
        while q:
          b, i, j, steps = q.popleft()

          bstr = str(b)
          if bstr in visited:
            continue
          visited.add(bstr)

          if bstr == final_state:
            return steps
          
          for ii, jj in get_neighbours(i, j):
            nb = copy.deepcopy(b)
            nb[ii][jj], nb[i][j] = nb[i][j], nb[ii][jj]
            q.append((nb, ii, jj, steps+1))

        return -1

    # def slidingPuzzle(self, board: List[List[int]]) -> int:
    #     final_state = str([
    #       [1, 2, 3],
    #       [4, 5, 0]
    #     ])
    #     # print(final_state)

    #     def get_neighbours(i: int, j: int) -> List[List[int]]:
    #       out = []
    #       for y, x in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
    #         if min(y, x) < 0 or y > 1 or x > 2:
    #           continue
    #         out.append((y, x))
    #       return out
        
    #     final_idx = {
    #       1: [0, 0],
    #       2: [0, 1],
    #       3: [0, 2],
    #       4: [1, 0],
    #       5: [1, 1],
    #     }
    #     # Heuristic score for the current board. Lower score is better
    #     def heuristic(board):
    #       score = 0
    #       for i, row in enumerate(board):
    #         for j, n in enumerate(row):
    #           if n > 0:
    #             final_i, final_j = final_idx[n]
    #             score += abs(final_i - i)
    #             score += abs(final_j - j)
    #       return score

    #     pq = []
    #     for i, row in enumerate(board):
    #       for j, n in enumerate(row):
    #         if n == 0:
    #           pq.append((heuristic(board), board, i, j, 0))
        
    #     visited = set()
    #     distance = defaultdict(lambda: float('inf'))
    #     while pq:
    #       _, b, i, j, steps = heapq.heappop(pq)

    #       bstr = str(b)
    #       distance[bstr] = min(distance[bstr], steps)
    #       if bstr in visited:
    #         continue
    #       visited.add(bstr)

    #       if bstr == final_state:
    #         continue
          
    #       for ii, jj in get_neighbours(i, j):
    #         nb = copy.deepcopy(b)
    #         nb[ii][jj], nb[i][j] = nb[i][j], nb[ii][jj]
    #         heapq.heappush(pq, (heuristic(nb), nb, ii, jj, distance[bstr]+1))

    #     return distance[final_state] if distance[final_state] != float('inf') else -1
        