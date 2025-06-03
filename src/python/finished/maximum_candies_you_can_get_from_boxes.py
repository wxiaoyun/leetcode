from typing import List

# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        # For a box to be opened
        # 1. It needs to be accessible (dependency 1)
        # 2. It needs to be open or openable (via key) (dependency 2)

        OPEN = 1
        CLOSE = 0
        KEY_DEP_MASK = 0b10
        RM_KEY_DEP_MASK = 0b01
        REACH_DEP_MASK = 0b01
        RM_REACH_DEP_MASK = 0b10
        root = set(initialBoxes)

        N = len(status)
        dep = [0] * N
        for n in range(N):
            if status[n] == CLOSE:
                dep[n] = dep[n] | KEY_DEP_MASK

            if n not in root:
                dep[n] = dep[n] | REACH_DEP_MASK

        frontier = []
        for n, d in enumerate(dep):
            if d == 0:
                frontier.append(n)

        visited = set()
        total = 0
        while frontier:
            n = frontier.pop()
            if n in visited:
                continue
            visited.add(n)

            total += candies[n]

            # remove key dependency for neighbour
            for nb in keys[n]:
                dep[nb] = dep[nb] & RM_KEY_DEP_MASK
                if dep[nb] == 0:
                    frontier.append(nb)

            # remove reach dependency for neighbour
            for nb in containedBoxes[n]:
                dep[nb] = dep[nb] & RM_REACH_DEP_MASK
                if dep[nb] == 0:
                    frontier.append(nb)

        return total
