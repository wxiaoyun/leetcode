from typing import List, Tuple

# https://leetcode.com/problems/predict-the-winner/


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        P1, P2 = 0, 1
        dp = {}

        def play(turn: int, l: int, r: int) -> Tuple[int, int]:
            if l >= r:
                return [0, 0]

            key = (turn, l, r)
            if key in dp:
                return dp[key]

            p_idx, opp_idx = 0, 1
            if turn == P2:
                p_idx, opp_idx = opp_idx, p_idx

            lscore, rscore = nums[l], nums[r - 1]

            take_left_score = play(turn ^ 1, l + 1, r)[:]
            take_right_score = play(turn ^ 1, l, r - 1)[:]

            take_left_score[p_idx] += lscore
            take_right_score[p_idx] += rscore

            best = [-1, -1]
            if take_left_score[p_idx] > take_right_score[p_idx]:
                best = take_left_score
            elif take_left_score[p_idx] < take_right_score[p_idx]:
                best = take_right_score
            elif take_left_score[opp_idx] < take_right_score[opp_idx]:
                best = take_left_score
            elif take_left_score[opp_idx] > take_right_score[opp_idx]:
                best = take_right_score
            else:
                best = take_left_score
            dp[key] = best
            # print(turn, l, r, best)
            return best

        scores = play(P1, 0, len(nums))
        # print(scores)
        return scores[0] >= scores[1]
