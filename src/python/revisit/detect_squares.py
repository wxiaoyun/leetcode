from collections import defaultdict
from typing import List

# https://leetcode.com/problems/detect-squares/


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        p = (x, y)
        self.points[p] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        x, y = point
        for xx, yy in self.points.keys():
            if xx == x and yy == y:
                continue
            dx, dy = xx - x, yy - y
            if abs(dx) != abs(dy):
                continue

            a = (xx, yy)
            b = (xx, y)
            c = (x, yy)
            cnt += self.points[a] * self.points.get(b, 0) * self.points.get(c, 0)
        return cnt


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
