# https://leetcode.com/problems/binary-gap/


class Solution:
    def binaryGap(self, n: int) -> int:
        prev_one = 64
        cur_idx = 0

        best = 0
        cur = n
        while cur:
            bit = cur & 1
            cur >>= 1
            if bit == 1:
                best = max(best, cur_idx - prev_one)
                prev_one = cur_idx
            cur_idx += 1

        return best
