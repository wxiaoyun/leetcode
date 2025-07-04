from typing import List

# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # 1 = 0 op (1)
        # 2 = 1 op (10) (1 char of 0th op + applying 1st op)
        # 3 = 2 op (11) (1 char of 1st op + applying 2nd op)
        # 4 = 2 op (100) (2 char of 1st op + applying 2nd op)
        # - ((1 char of 0th op + applying 1st op) + applying 2nd op)
        # - ((0 + applying 1st op) + applying 2nd op)
        # 5 = 3 op (101) (1 char of 2nd op + applying 3rd op)
        # - ((1 char of 1st op + applying 2nd op) + applying 3rd op)
        # - ((0 + applying 2nd op) + applying 3rd op)

        # 10 - 0b1010
        # - 3rd char of 3rd op (010)

        k -= 1
        shifts = 0
        i = 0
        while k > 0:
            rem = k % 2
            k = k >> 1

            if rem == 1 and operations[i] == 1:
                # apply ith operation
                shifts += 1

            i += 1

        return chr(ord("a") + (shifts % 26))
