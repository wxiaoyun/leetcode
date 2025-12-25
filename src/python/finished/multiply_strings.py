from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def mul(n: List[int], digit: int) -> List[int]:
            carry = 0
            for i in range(len(n)):
                product = n[i] * digit + carry
                carry = product // 10
                n[i] = product % 10

            if carry > 0:
                n.append(carry)
            return n

        def add(a: List[int], b: List[int]) -> List[int]:
            if len(b) > len(a):
                a, b = b, a

            # len(a) >= len(b)
            alen = len(a)
            carry = 0
            for i in range(alen + 1):
                if not carry and i >= len(b):
                    break
                anum = a[i] if i < len(a) else 0
                bnum = b[i] if i < len(b) else 0
                summ = anum + bnum + carry
                carry = summ // 10

                if i < len(a):
                    a[i] = summ % 10
                else:
                    a.append(summ % 10)

            return a

        a = [int(c) for c in num1]
        a.reverse()

        ln = len(num2)
        res = []
        for i in range(ln):
            ch = int(num2[ln - i - 1])

            tmp = [0] * i
            tmp.extend(a)

            prod = mul(tmp, ch)
            res = add(res, prod)

        res.reverse()
        return "".join(str(d) for d in res)
