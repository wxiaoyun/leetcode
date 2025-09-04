# https://leetcode.com/problems/find-closest-person/


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz_t = abs(x - z)
        yz_t = abs(y - z)

        if xz_t < yz_t:
            return 1
        elif xz_t > yz_t:
            return 2
        return 0
