from typing import List

# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in reversed(range(len(digits))):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break

            digits[i] = 0
            carry = 1

        if carry:
            digits.insert(0, 1)

        return digits
