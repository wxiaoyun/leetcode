from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        STONE = "#"
        OBS = "*"
        EMPTY = "."
        m, n = len(boxGrid), len(boxGrid[0])

        right_obs = [[n] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in reversed(range(n)):
                right_obs[i][j] = j if boxGrid[i][j] == OBS else right_obs[i][j + 1]
        # [print(row) for row in right_obs]

        ans = [boxGrid[i][:] for i in range(m)]
        for i in range(m):
            next_obs = n
            for j in reversed(range(n)):
                # print(i, j, next_obs)
                next_obs = min(next_obs, right_obs[i][j])
                if boxGrid[i][j] == OBS:
                    next_obs = n
                if boxGrid[i][j] != STONE:
                    continue

                ans[i][j] = EMPTY
                ans[i][next_obs - 1] = STONE
                next_obs = next_obs - 1
                # print(f"from {j} to {next_obs - 1}")

        ans_trans = [[ans[m - 1 - i][j] for i in range(m)] for j in range(n)]
        return ans_trans


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R = len(box)
        C = len(box[0])

        for row in box:
            row.append("*")

        for r in range(R):
            for c in reversed(range(C + 1)):
                if box[r][c] != "*":
                    continue
                stone_count = 0
                for i in reversed(range(c)):
                    if box[r][i] == "*":
                        break
                    if box[r][i] == "#":
                        stone_count += 1
                    box[r][i] = "."
                for i in range(stone_count):
                    box[r][c - 1 - i] = "#"

        res = []
        for c in range(C):
            res.append([])
            for r in range(R):
                res[-1].append(box[R - 1 - r][c])

        return res
