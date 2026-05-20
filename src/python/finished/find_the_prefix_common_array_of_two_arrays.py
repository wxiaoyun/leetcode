from collections import Counter
from typing import List

# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        assert n == len(B)

        cnt = Counter()
        C = [0] * n

        for i in range(n):
            C[i] = C[i - 1] if i > 0 else 0

            a, b = A[i], B[i]

            cnt[a] += 1
            cnt[b] -= 1

            if cnt[a] == 0:
                C[i] += 1
            if a != b and cnt[b] == 0:
                C[i] += 1
        return C


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        seen = set()
        aa = set()
        bb = set()
        res = []

        for i in range(N):
            cha = A[i]
            chb = B[i]

            aa.add(cha)
            bb.add(chb)

            if cha not in seen and cha in bb:
                seen.add(cha)
            if chb not in seen and chb in aa:
                seen.add(chb)

            res.append(len(seen))

        return res
