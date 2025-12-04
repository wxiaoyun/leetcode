from typing import List


# https://leetcode.com/problems/count-collisions-on-a-road/


class Solution:
    def countCollisions(self, directions: str) -> int:
        # Observation:
        # 1. if two cars are moving in the same direction without
        #    blockage, then will never collide
        # 2. if a car is moving toward a stationary car, or a car travelling towards
        #    it, they will eventually collide


        l_collisions = 0
        obstacles = 0
        for dirc in directions:
            match dirc:
                case "L":
                    if obstacles > 0:
                        l_collisions += 1
                case _:
                    obstacles += 1

        r_collisions = 0
        obstacles = 0
        for dirc in reversed(directions):
            match dirc:
                case "R":
                    if obstacles > 0:
                        r_collisions += 1
                case _:
                    obstacles += 1

        return l_collisions + r_collisions