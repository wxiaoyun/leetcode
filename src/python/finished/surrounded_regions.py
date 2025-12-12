from collections import deque
from typing import List

# https://leetcode.com/problems/surrounded-regions/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        q = deque()
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    q.append((i, j))
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == "O":
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            if board[i][j] != "O":
                continue
            board[i][j] = "R"

            for dr, dc in [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]:
                rr, cc = i + dr, j + dc

                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                q.append((rr, cc))

        for i in range(m):
            for j in range(n):
                if board[i][j] != "R":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"

        return None
