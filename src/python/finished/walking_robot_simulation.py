from typing import List

# https://leetcode.com/problems/walking-robot-simulation/


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        TURN_LEFT, TURN_RIGHT = -2, -1
        NORTH, EAST, SOUTH, WEST = list(range(4))
        dir_delta = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
        }
        ob_set = set((x, y) for x, y in obstacles)

        ans = 0
        cur_x, cur_y, dir = (0, 0, NORTH)
        for cmd in commands:
            if cmd == TURN_LEFT:
                dir = (dir - 1) % 4
            elif cmd == TURN_RIGHT:
                dir = (dir + 1) % 4
            else:
                steps = cmd
                dx, dy = dir_delta[dir]
                for _ in range(steps):
                    next_x , next_y = cur_x + dx, cur_y + dy
                    if (next_x, next_y) in ob_set:
                        break
                    cur_x, cur_y = next_x, next_y

            ans = max(ans, cur_x**2 + cur_y**2)

        return ans
