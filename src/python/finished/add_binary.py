# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0:
            total = int(a[i] if i >= 0 else 0) + int(b[j] if j >= 0 else 0) + carry
            rem = total & 1
            carry = (total >> 1) & 1

            res.append(str(rem))
            i -= 1
            j -= 1

        if carry:
            res.append(str(carry))

        return "".join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a)
        blen = len(b)
        abmax = max(alen, blen)

        res = []
        carry = 0
        for i in range(abmax):
            tmp = carry

            if i < alen and a[alen - 1 - i] == "1":
                tmp += 1
            if i < blen and b[blen - 1 - i] == "1":
                tmp += 1

            if tmp > 1:
                tmp = tmp % 2
                carry = 1
            else:
                carry = 0

            res.append(str(tmp))

        if carry:
            res.append("1")

        return "".join(reversed(res))
