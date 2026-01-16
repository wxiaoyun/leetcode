# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/


from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        rows = [0]
        rows.extend(r - 1 for r in hFences)
        rows.append(m - 1)

        row_len_set = set()
        for i in range(len(rows)):
            left = rows[i]
            for j in range(i + 1, len(rows)):
                right = rows[j]
                row_len_set.add(abs(right - left))
        row_lens = sorted(list(row_len_set))

        cols = [0]
        cols.extend(c - 1 for c in vFences)
        cols.append(n - 1)

        col_len_set = set()
        for i in range(len(cols)):
            left = cols[i]
            for j in range(i + 1, len(cols)):
                right = cols[j]
                col_len_set.add(abs(right - left))
        col_lens = sorted(list(col_len_set))

        i, j = len(row_lens) - 1, len(col_lens) - 1
        while i >= 0 and j >= 0:
            while i >= 0 and row_lens[i] > col_lens[j]:
                i -= 1
            if i < 0:
                break

            while j >= 0 and row_lens[i] < col_lens[j]:
                j -= 1
            if j < 0:
                break

            if row_lens[i] > col_lens[j]:
                continue

            # row_lens[i] == col_lens[j]
            return (row_lens[i] * col_lens[j]) % (int(1e9) + 7)
        return -1
