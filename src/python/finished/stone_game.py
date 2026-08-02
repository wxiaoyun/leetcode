from typing import List

# https://leetcode.com/problems/stone-game


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        ALICE, BOB = 0, 1

        def play(turn: int, l: int, r: int) -> int:
            if l >= r:
                return 0

            key = (turn, l, r)
            if key in dp:
                return dp[key]

            SIGN = 1 if turn == ALICE else -1

            left, right = piles[l], piles[r - 1]
            take_left_diff = play(turn ^ 1, l + 1, r)
            take_right_diff = play(turn ^ 1, l, r - 1)

            left_score = take_left_diff * SIGN + left
            right_score = take_right_diff * SIGN + right

            best_score = SIGN * max(left_score, right_score)
            dp[key] = best_score
            # print(f"{"ALICE" if turn == ALICE else "BOB"} {l} {r} {best_score}")
            return best_score

        return play(ALICE, 0, len(piles)) > 0
