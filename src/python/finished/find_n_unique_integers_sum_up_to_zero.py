# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = [0] * n

        i = 0
        if n % 2 == 1:
            i += 1

        while i < n:
            prev = -ret[i - 1]
            ret[i] = prev + 1
            ret[i + 1] = -prev - 1
            i += 2

        return ret
