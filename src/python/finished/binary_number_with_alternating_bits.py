# https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur = n
        prev = (cur & 1) ^ 1
        while cur != 0:
            if (cur & 1) == prev:
                return False

            prev = cur & 1
            cur >>= 1

        return True
