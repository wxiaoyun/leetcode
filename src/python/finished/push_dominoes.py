from collections import deque

# https://leetcode.com/problems/push-dominoes


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        for i, d in enumerate(dominoes):
            match d:
                case ".":
                    continue
                case "L":
                    q.append((i, -1))
                case "R":
                    q.append((i, 1))

        ds = ["."] * len(dominoes)
        while q:
            state = {}
            level = len(q)

            for _ in range(level):
                i, d = q.popleft()
                if i < 0 or i >= len(ds):
                    continue
                if d == 0 or ds[i] != ".":
                    continue
                ds[i] = "L" if d < 0 else "R"

                j = i + d
                state[j] = state.get(j, 0) + d

            for j, d in state.items():
                if d == 0:
                    continue
                q.append((j, d))

        return "".join(ds)
