from typing import List

# https://leetcode.com/problems/number-of-paths-with-max-score/


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        OBS = "X"
        MOD = 10**9 + 7
        n, m = len(board), len(board[0])
        maxs = [[0] * m for _ in range(n)]
        ways_max = [[0] * m for _ in range(n)]
        ways_max[n - 1][m - 1] = 1
        # print(n, m)

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # print(r, c)
                if board[r][c] == OBS:
                    continue

                cell_val = 0 if board[r][c] in "ESX" else int(board[r][c])
                for rr, cc in [
                    (r + 1, c),
                    (r, c + 1),
                    (r + 1, c + 1),
                ]:
                    if rr >= n or cc >= m or ways_max[rr][cc] == 0:
                        continue

                    cur_max = maxs[r][c]
                    new_max = maxs[rr][cc] + cell_val
                    if cur_max > new_max:
                        pass
                    elif cur_max == new_max:
                        ways_max[r][c] += ways_max[rr][cc]
                    else:  # cur_max < new_max
                        maxs[r][c] = new_max
                        ways_max[r][c] = ways_max[rr][cc]
                    ways_max[r][c] %= MOD
                # print(maxs)
                # print(ways_max)

        return maxs[0][0], ways_max[0][0]
