from collections import deque
from typing import List

# https://leetcode.com/problems/snakes-and-ladders


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        R = len(board)
        C = len(board[0])
        DEST = R * C

        label_to_coord = {}
        for r in range(R):
            rC = r * C
            row = [rC + c + 1 for c in range(C)]
            if r % 2 == 1:
                row.reverse()

            for i, label in enumerate(row):
                label_to_coord[label] = (r, i)

        visited = set()
        q = deque([1])
        depth = 0
        while q:
            llen = len(q)

            for _ in range(llen):
                l = q.popleft()

                if l in visited:
                    continue
                visited.add(l)

                if l == DEST:
                    return depth

                for ll in range(l + 1, min(l + 6, DEST) + 1):
                    r, c = label_to_coord[ll]
                    if board[r][c] >= 0:
                        q.append(board[r][c])
                    else:
                        q.append(ll)

            depth += 1

        return -1
