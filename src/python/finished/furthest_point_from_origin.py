# https://leetcode.com/problems/furthest-point-from-origin/


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        best = -1

        cur = 0
        for mv in moves:
            if mv in "L_":
                cur += 1
            else:
                cur -= 1
        best = max(best, cur)

        cur = 0
        for mv in moves:
            if mv in "R_":
                cur += 1
            else:
                cur -= 1
        best = max(best, cur)

        return best
