# https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)

        res = []
        carry = 0
        for i in range(max(len1, len2)):
            n1 = int(num1[len1 - i - 1]) if i < len1 else 0
            n2 = int(num2[len2 - i - 1]) if i < len2 else 0

            summed = n1 + n2 + carry
            res.append(str(summed % 10))
            carry = summed // 10

        if carry > 0:
            res.append(str(carry))

        return "".join(reversed(res))
