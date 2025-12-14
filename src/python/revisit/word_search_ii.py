from collections import defaultdict

from typings import List


class Trie:
    def __init__(self):
        self.end = False
        self.children = defaultdict(Trie)

    def insert(self, w: str, i: int = 0):
        cur = self
        while i < len(w):
            ch = w[i]
            child = cur.children[ch]
            cur = child
            i += 1
        cur.end = True

    def find(self, w: str, i: int = 0) -> bool:
        if i >= len(w):
            return self.end

        ch = w[i]
        if ch not in self.children:
            return False

        return self.children[ch].find(w, i + 1)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        if m == 1 and n == 1:
            return [w for w in words if w == board[0][0]]

        t = Trie()
        for w in words:
            t.insert(w)

        on_board = set()

        def exists(board, t, r, c, builder, visited):
            if t.end:
                t.end = False
                on_board.add("".join(builder))

            ch = board[r][c]
            if ch not in t.children:
                return
            tt = t.children[ch]

            node = (r, c)
            if node in visited:
                return
            visited.add(node)

            for rr, cc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                builder.append(ch)
                exists(board, tt, rr, cc, builder, visited)
                builder.pop()

            visited.remove(node)

        for r in range(m):
            for c in range(n):
                exists(board, t, r, c, [], set())
        return list(on_board)


# O(|w| * mn * 4^mn), TLE
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        starts = defaultdict(list)
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                starts[ch].append((i, j))

        def exists(word: str, i: int, r: int, c: int, visited: set) -> bool:
            if (r, c) in visited:
                return False
            visited.add((r, c))

            if i == len(word) - 1:
                return board[r][c] == word[i]

            if board[r][c] != word[i]:
                visited.remove((r, c))
                return False

            for dr, dc in [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ]:
                rr, cc = dr + r, dc + c

                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                if exists(word, i + 1, rr, cc, visited):
                    return True

            visited.remove((r, c))
            return False

        on_board = []
        for w in words:
            for i, j in starts[w[0]]:
                if exists(w, 0, i, j, set()):
                    on_board.append(w)
                    break
        return on_board
