from typing import List

# https://leetcode.com/problems/robot-collisions/


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()

        LEFT, RIGHT = "L", "R"

        survivors = []

        # stack of right going robots
        stack = []
        for i in range(n):
            _, h, d, j = robots[i]

            if d == RIGHT:
                stack.append((j, h))
                continue

            # d == LEFT
            while stack and h > 0:
                # print(i, stack, h, j)
                # print(survivors)
                i_left, h_left = stack.pop()

                if h_left > h:
                    h = 0
                    stack.append((i_left, h_left - 1))
                    break
                elif h_left == h:
                    h = 0
                    break
                else:  # h_left < h:
                    h -= 1

            if h > 0:
                survivors.append((j, h))

        survivors.extend(stack)
        survivors.sort()
        return [h for _, h in survivors]
