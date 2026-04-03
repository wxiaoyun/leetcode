from typing import List

# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        ROBOT = 1 << 0
        WALL = 1 << 1

        tmp = []
        tmp.extend((p, ROBOT, i) for i, p in enumerate(robots))
        tmp.extend((p, WALL, 0) for p in walls)
        tmp.sort()

        objects = []
        for i in range(len(tmp)):
            if i == 0:
                objects.append(tmp[i])
                continue

            pp, pty, pi = objects[-1]
            cp, cty, ci = tmp[i]

            if pp == cp:
                objects[-1] = (pp, pty | cty, pi | ci)
                continue

            objects.append(tmp[i])
        # print(objects)

        # dp[i] = maximum walls destroyed by objects[:i]
        dp = [0] * (len(objects) + 1)

        for i, (position, ty, robot_index) in enumerate(objects):
            ii = i + 1
            dp[ii] = max(dp[ii], dp[i])

            if ty & ROBOT == 0:
                continue

            cur_dp = dp[ii]
            robot_range = distance[robot_index]

            # case: shoot left
            j = i
            n_walls = 0
            while j >= 0 and objects[j][0] >= position - robot_range:
                if j != i and objects[j][1] & ROBOT:
                    # print("left: HIT ROBOT", j, i)
                    break
                if objects[j][1] & WALL:
                    n_walls += 1
                dp[ii] = max(dp[ii], dp[j] + n_walls)
                j -= 1
            # print(i, "shoot left", dp)

            # case: shoot right
            j = i
            n_walls = 0
            while j < len(objects) and objects[j][0] <= position + robot_range:
                if j != i and objects[j][1] & ROBOT:
                    # print("right: HIT ROBOT", j, i)
                    break
                if objects[j][1] & WALL:
                    n_walls += 1
                j += 1
                dp[j] = max(dp[j], cur_dp + n_walls)

            # print(i, "shoot right", dp)

        # print(dp)
        return dp[-1]
