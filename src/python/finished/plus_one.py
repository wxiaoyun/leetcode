from typing import List

# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1

        for i in reversed(range(len(digits))):
            if carry_over == 0:
                break

            digits[i] += carry_over
            if digits[i] < 10:
                carry_over = 0
                continue

            digits[i] = 0
            carry_over = 1

        if carry_over:
            digits.insert(0, 1)
        return digits
