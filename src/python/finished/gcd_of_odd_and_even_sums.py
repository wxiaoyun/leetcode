from typing import List

# https://leetcode.com/problems/gcd-of-odd-and-even-sums


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = (2 * 1 + (n - 1) * 2) // 2 * n
        sumEven = sumOdd + n
        # print(sumOdd, sumEven)

        def factorize(num: int) -> List[int]:
            ofact = []
            fact = 2
            while num > 1:
                while num % fact == 0:
                    ofact.append(fact)
                    num //= fact
                fact += 1
            return ofact

        ofact = factorize(sumOdd)
        efact = factorize(sumEven)

        gcd = 1
        i, j = 0, 0
        while i < len(ofact) and j < len(efact):
            if ofact[i] == efact[j]:
                gcd *= ofact[i]
                i += 1
                j += 1
                continue

            if ofact[i] < efact[j]:
                i += 1
            else:
                j += 1

        return gcd
