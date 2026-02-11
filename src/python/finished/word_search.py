from typing import List

# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])

        def helper(i: int, j: int, w: int) -> bool:
            if w >= len(word):
                return True

            if min(i, j) < 0 or i >= nrows or j >= ncols:
                return False

            if not board[i][j]:
                return False

            c = board[i][j]
            if word[w] != c:
                return False
            board[i][j] = ""

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if helper(i + di, j + dj, w + 1):
                    return True

            board[i][j] = c
            return False

        for i in range(nrows):
            for j in range(ncols):
                if helper(i, j, 0):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited: set, r: int, c: int, i: int) -> bool:
            if i >= len(word):
                return True
            if min(r, c) < 0 or r >= len(board) or c >= len(board[0]):
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[i]:
                return False

            visited.add((r, c))
            for rr, cc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                if dfs(visited, rr, cc, i + 1):
                    return True
            visited.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(set(), r, c, 0):
                    return True
        return False
