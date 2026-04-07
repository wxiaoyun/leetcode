# https://leetcode.com/problems/walking-robot-simulation-ii/


from typing import List

EAST, SOUTH, WEST, NORTH = list(range(4))
DIR_DELTA = {
    EAST: (0, 1),
    WEST: (0, -1),
    NORTH: (1, 0),
    SOUTH: (-1, 0),
}
DIR_STR = {
    EAST: "East",
    WEST: "West",
    NORTH: "North",
    SOUTH: "South",
}


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        cycle_indices = []
        for x in range(width):
            cycle_indices.append((x, 0))
        for y in range(1, height):
            cycle_indices.append((width - 1, y))
        for x in reversed(range(width - 1)):
            cycle_indices.append((x, height - 1))
        for y in reversed(range(height - 1)):
            cycle_indices.append((0, y))
        self.cycle_indices = cycle_indices
        self.cycle_index = 0
        self.cycle_len = (width - 1) * 2 + (height - 1) * 2

        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.cycle_index = (self.cycle_index + num) % self.cycle_len

    def getPos(self) -> List[int]:
        return self.cycle_indices[self.cycle_index]

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        if 0 < self.cycle_index and self.cycle_index <= self.width - 1:
            return "East"
        if (
            self.width - 1 < self.cycle_index
            and self.cycle_index <= self.width + self.height - 2
        ):
            return "North"
        if (
            self.width + self.height - 2 < self.cycle_index
            and self.cycle_index <= self.width * 2 + self.height - 3
        ):
            return "West"
        if (
            self.width * 2 + self.height - 3 < self.cycle_index
            and self.cycle_index < self.cycle_len
        ):
            return "South"
        if self.cycle_index == 0:
            return "South"

    # def inbound(self, x: int, y: int) -> bool:
    #     return min(x, y) >= 0 and x < self.width and y < self.height

    # def step(self, num: int) -> None:
    #     # print("STEP", num, (self.x, self.y, self.dir))
    #     assert self.inbound(self.x, self.y)

    #     dy, dx = DIR_DELTA[self.dir]
    #     next_y, next_x = self.y + num * dy, self.x + num * dx

    #     if self.inbound(next_x, next_y):
    #         self.x, self.y = next_x, next_y
    #         return None

    #     bounded_y, bounded_x = next_y, next_x
    #     if bounded_y >= self.height:
    #         bounded_y = self.height - 1
    #     elif bounded_y < 0:
    #         bounded_y = 0
    #     if bounded_x >= self.width:
    #         bounded_x = self.width - 1
    #     elif bounded_x < 0:
    #         bounded_x = 0

    #     # print("OUT OF BOUND", (next_x, next_y))
    #     # print("TRIM", (bounded_x, bounded_y))

    #     num_taken = max(abs(self.y - bounded_y), abs(self.x - bounded_x))
    #     self.x, self.y = bounded_x, bounded_y
    #     self.dir = (self.dir - 1) % 4
    #     self.step(num - num_taken)

    # def getPos(self) -> List[int]:
    #     return [self.x, self.y]

    # def getDir(self) -> str:
    #     return DIR_STR[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
