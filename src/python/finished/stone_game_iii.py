from typing import List

# https://leetcode.com/problems/stone-game-iii


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ALICE, BOB = 0, 1
        dp = {}

        def play(turn: int, i: int) -> int:
            if i >= len(stoneValue):
                return 0

            key = (turn, i)
            if key in dp:
                return dp[key]

            SIGN = 1
            if turn == BOB:
                SIGN = -1

            best = -(1 << 64)
            values = 0
            for j in range(i, min(len(stoneValue), i + 3)):
                values += stoneValue[j]
                game_scores = play(turn ^ 1, j + 1) * SIGN
                best = max(best, values + game_scores)
            # print(f"{"A" if turn == ALICE else "B"} {i} {best * SIGN}")
            dp[key] = best * SIGN
            return dp[key]

        result = play(ALICE, 0)
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        return "Tie"
