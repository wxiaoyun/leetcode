# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # observation: any integer can be represented in binary
        #
        # the problem is essentially asking:
        # what is the minimum k such that:
        # (num1 - k * num2) can be represented by k nonnegative powers of 2

        def count_one_bits(n: int) -> int:
            count = 0
            while n > 0:
                count += n & 1
                n = n >> 1
            return count

        n1_cur = num1
        n2_removed = 0

        while n1_cur >= n2_removed and n2_removed < count_one_bits(n1_cur):
            n1_cur -= num2
            n2_removed += 1
        return n2_removed if n1_cur >= n2_removed else -1
