# https://leetcode.com/problems/alice-and-bob-playing-flower-game/


class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        # 1, (n - 1), (m - 1), 1
        return n * m // 2
