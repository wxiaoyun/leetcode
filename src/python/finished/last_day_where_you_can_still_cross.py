from collections import deque
from typing import List

# https://leetcode.com/problems/last-day-where-you-can-still-cross


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, a):
        ap = self.parent.setdefault(a, a)
        if ap == a:
            return ap

        app = self.find(ap)
        self.parent[a] = app
        return app

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap == bp:
            return

        apr, bpr = self.rank.setdefault(ap, 1), self.rank.setdefault(bp, 1)
        if apr > bpr:
            self.parent[bp] = ap
            self.rank[ap] += bpr
        else:
            self.parent[ap] = bp
            self.rank[bp] += apr
        return


# O(V α(V)) ≈ O(V)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        waters = set((r - 1, c - 1) for r, c in cells)

        uf = UF()
        START = (-1, -1)
        END = (row, col)

        for c in range(col):
            cell_start = (0, c)
            uf.union(START, cell_start)

            cell_end = (row - 1, c)
            uf.union(END, cell_end)

        for r in range(row):
            for c in range(col):
                cell = (r, c)
                if cell in waters:
                    continue

                for nb in [
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ]:
                    if nb in waters:
                        continue

                    uf.union(cell, nb)

        for i in reversed(range(len(cells))):
            r, c = cells[i]
            r, c = r - 1, c - 1
            cell = (r, c)
            waters.remove(cell)
            for nb in [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]:
                if nb in waters:
                    continue

                uf.union(cell, nb)

            if uf.find(START) == uf.find(END):
                return i

        return -1


# O(VlogV)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def possible(row: int, col: int, cells: List[List[int]], day: int) -> bool:
            waters = set()
            for r, c in cells[:day]:
                waters.add((r - 1, c - 1))

            visited = set()
            q = deque((0, c) for c in range(col) if (0, c) not in waters)
            while q:
                cell = q.popleft()
                if cell in visited:
                    continue
                visited.add(cell)

                r, c = cell
                if r == row - 1:
                    return True

                for rr, cc in [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1),
                ]:
                    if min(rr, cc) < 0 or rr >= row or cc >= col:
                        continue

                    if (rr, cc) in waters:
                        continue

                    q.append((rr, cc))

            return False

        l, r = 0, len(cells)
        ans = len(cells)
        while l < r:
            m = l + (r - l) // 2
            # TTTTTTTTTTTTTFFFFF
            # l       m        r
            if possible(row, col, cells, m):
                ans = m
                l = m + 1
            # TTTTTTTFFFFFFFFFFF
            # l       m        r
            else:
                r = m

        return ans
