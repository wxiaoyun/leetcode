import re
from typing import Optional, Tuple

# https://leetcode.com/problems/design-spreadsheet/


CELL_REG = re.compile(r"^([A-Z]+)([0-9]+)$")
FORMULA_REG = re.compile(r"^=([A-Z]*[0-9]+)\+([A-Z]*[0-9]+)$")


def parse_cell(cell: str) -> Optional[Tuple[int, int]]:
    matches = re.search(CELL_REG, cell)
    if matches is None:
        return None
    groups = matches.groups()
    if len(groups) < 2:
        return None
    col, row = groups[0], groups[1]
    return int(row) - 1, (ord(col) - ord("A"))


class Spreadsheet:

    def __init__(self, rows: int):
        grid = [[0] * 26 for _ in range(rows)]
        self.grid = grid

    def setCell(self, cell: str, value: int) -> None:
        row, col = parse_cell(cell)
        if min(row, col) < 0 or row >= len(self.grid) or col >= len(self.grid[0]):
            raise Exception("Illegal cell, index out of bound")

        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        if re.search(r"^[0-9]+$", formula) is not None:
            return int(formula)

        if re.search(CELL_REG, formula) is not None:
            row, col = parse_cell(formula)
            return self.grid[row][col]

        matches = re.search(FORMULA_REG, formula)
        if matches is None:
            raise Exception("Illegal formula format")
        groups = matches.groups()
        if len(groups) < 2:
            raise Exception("Illegal formula")

        return self.getValue(groups[0]) + self.getValue(groups[1])


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
