from typing import List

# https://leetcode.com/problems/cinema-seat-allocation/


index = [[] for _ in range(10 + 1)]

for i, start in enumerate([2, 4, 6]):
    for j in range(start, start + 4):
        index[j].append(i)


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_reservation = {}

        for r, s in reservedSeats:
            res = row_reservation.setdefault(r, [False] * 3)
            for idx in index[s]:
                res[idx] = True

        n_seated = 0
        free_rows = n
        for r in row_reservation.keys():
            free_rows -= 1

            for idx, is_reserved in enumerate(row_reservation[r]):
                if is_reserved:
                    continue

                n_seated += 1
                if idx + 1 < 3:
                    row_reservation[r][idx + 1] = True

        n_seated += free_rows * 2
        return n_seated
