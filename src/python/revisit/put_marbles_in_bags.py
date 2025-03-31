from typing import List

# https://leetcode.com/problems/put-marbles-in-bags


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        N = len(weights)
        splits = [(weights[i] + weights[i + 1]) for i in range(N - 1)]
        splits.sort()
        n_splits = k - 1
        return sum(splits[-n_splits:]) - sum(splits[:n_splits])
