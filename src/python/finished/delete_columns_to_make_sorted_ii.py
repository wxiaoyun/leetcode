from typing import List

# https://leetcode.com/problems/delete-columns-to-make-sorted-ii


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        OK = 1
        TIE = 2
        BAD = 3

        ndel = 0
        prev_col = -1
        tie_idx = list((i - 1, i) for i in range(1, n))
        for j in range(m):
            tmp = []
            state = OK
            for prev_i, i in tie_idx:
                prev_left = "" if prev_col < 0 else strs[prev_i][prev_col]
                cur_left = "" if prev_col < 0 else strs[i][prev_col]

                if prev_left < cur_left:
                    continue
                assert prev_left == cur_left

                prev = strs[prev_i][j]
                cur = strs[i][j]

                if prev < cur:
                    continue

                if prev == cur:
                    state = TIE
                    tmp.append((prev_i, i))
                    continue

                state = BAD
                break

            match state:
                case s if s == OK:
                    return ndel
                case s if s == TIE:
                    tie_idx = tmp
                    prev_col = j
                case s:
                    assert s == BAD
                    ndel += 1

        return ndel
