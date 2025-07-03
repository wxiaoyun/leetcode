# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i


class Solution:
    def kthCharacter(self, k: int) -> str:
        cur = [0]
        while len(cur) < k:
            l = len(cur)
            for i in range(l):
                cur.append((cur[i] + 1) % 26)
        return chr(ord("a") + cur[k - 1])
