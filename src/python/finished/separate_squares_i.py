from typing import List

# https://leetcode.com/problems/separate-squares-i/




# O(nlog(height_range))
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_diff(sqs: List[List[float]], cut: int) -> float:
            bot_sum, top_sum = 0.0, 0.0

            for y, l in sqs:
                bot, top = y, y + l

                if top <= cut:
                    bot_sum += l * l

                elif bot >= cut:
                    top_sum += l * l

                else:
                    top_sum += l * (top - cut)
                    bot_sum += l * (cut - bot)
            return bot_sum - top_sum

        EPS = 1e-5
        squares = sorted((float(y), float(l)) for _, y, l in squares)
        l, r = squares[0][0], max(y + l for y, l in squares)
        while r - l > EPS:
            m = (l + r) / 2

            diff = area_diff(squares, m)
            if diff < 0:
                # we need to include more squares below the cut
                l = m
            else:
                r = m

        return l
