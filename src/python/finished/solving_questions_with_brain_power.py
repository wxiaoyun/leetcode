from typing import List

# https://leetcode.com/problems/solving-questions-with-brainpower


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [-1] * N

        def compute(i: int) -> int:
            if i >= N:
                return 0

            if dp[i] > 0:
                return dp[i]

            p, b = questions[i]
            best = max(p + compute(i + b + 1), compute(i + 1))

            dp[i] = best
            return best

        return compute(0)
