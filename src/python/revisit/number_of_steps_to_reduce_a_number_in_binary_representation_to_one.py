# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one


class Solution:
    def numSteps(self, s: str) -> int:
        bits = [int(ch) for ch in s]

        carry = 0
        steps = 0
        while bits:
            b = bits.pop() + carry

            bit = b & 1
            carry = b >> 1

            if bit != 0 and bits:
                assert carry == 0
                steps += 1
                carry = 1

            if bits:
                steps += 1

        return steps + carry
