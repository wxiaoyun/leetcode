from typing import List


# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dp = {}

        def check(r: int, c: int) -> int:
            if grid[r][c] != 1:
                return 0

            directions = [
                (1, 1),
                (1, -1),
                (-1, -1),
                (-1, 1),
            ]
            seq = [2, 0]

            def helper(
                r: int,
                c: int,
                dir_idx: int = 0,
                seq_idx: int = 0,
                turns: int = 0,
            ) -> int:
                if min(r, c) < 0 or r >= R or c >= C or grid[r][c] != seq[seq_idx]:
                    return 0

                key = (r, c, dir_idx, seq_idx, turns)
                if key in dp:
                    return dp[key]

                next_seq_idx = (seq_idx + 1) % 2
                best = 0
                for dd in [0, 1]:
                    new_turns = turns + (0 if dd == 0 else 1)
                    if new_turns > 1:
                        continue

                    next_dir_idx = (dir_idx + dd) % 4
                    dr, dc = directions[next_dir_idx]
                    best = max(
                        best,
                        helper(r + dr, c + dc, next_dir_idx, next_seq_idx, new_turns),
                    )

                dp[key] = 1 + best
                return 1 + best

            return 1 + max(
                helper(r + directions[d][0], c + directions[d][1], d) for d in range(4)
            )

        return max(check(i // C, i % C) for i in range(R * C))
