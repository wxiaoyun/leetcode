# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/


class Solution:
    def maxOperations(self, s: str) -> int:
        # to maximize the number of operations, we need to use the least efficient strategy
        # -> the leftmost 1 with trailing zeros

        n = len(s)
        ones = 0
        swaps = 0
        for i, ch in enumerate(s):
            if ch == "1":
                ones += 1
                continue

            # ch == "0"
            is_end = i == (n - 1)
            is_next_one = i + 1 < n and s[i + 1] == "1"
            should_swap = is_end or is_next_one

            if not should_swap:
                continue

            swaps += ones

        return swaps
