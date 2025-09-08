# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contain_zero(n: int) -> bool:
            return "0" in str(n)

        for a in range(1, n):
            b = n - a
            if contain_zero(a) or contain_zero(b):
                continue
            return [a, b]
        return []
