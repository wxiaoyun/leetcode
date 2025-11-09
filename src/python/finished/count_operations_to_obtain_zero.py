# https://leetcode.com/problems/count-operations-to-obtain-zero/


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        ops = 0
        while a != 0 and b != 0:
            if a >= b:
                a -= b
            else:
                b -= a
            ops += 1
        return ops


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        return 1 + (
            self.countOperations(num1 - num2, num2)
            if num1 >= num2
            else self.countOperations(num1, num2 - num1)
        )
