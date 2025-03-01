# https://leetcode.com/problems/walking-robot-simulation

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:        
        dir_to_delta = {
          'N': (0, 1),
          'E': (1, 0),
          'S': (0, -1),
          'W': (-1, 0)
        }
        directions = ['N', 'E', 'S', 'W']
        dir_to_idx = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        obs = set([(x, y) for x, y in obstacles])

        def change_dir(cmd: int, dir: str) -> str:
          if cmd == -2:
            idx = dir_to_idx[dir]
            new_idx = (idx - 1) % len(directions)
            return directions[new_idx]

          if cmd == -1:
            idx = dir_to_idx[dir]
            new_idx = (idx + 1) % len(directions)
            return directions[new_idx]
          
          raise Exception("Invalid change direction command") 
        
        max_dist = 0
        i, j = 0, 0
        direction = 'N'
        for cmd in commands:
          if cmd < 0:
            direction = change_dir(cmd, direction)
            continue

          dist = cmd
          dx, dy = dir_to_delta[direction]

          for _ in range(dist):
            if (i + dx, j + dy) in obs:
              break
            i, j = i + dx, j + dy

          max_dist = max(max_dist, i**2 + j**2)
        
        return max_dist
