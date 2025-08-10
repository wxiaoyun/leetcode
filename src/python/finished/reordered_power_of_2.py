# https://leetcode.com/problems/reordered-power-of-2/

from collections import Counter


def key(nstr: str) -> str:
    builder = []
    for d, f in sorted(Counter(nstr).items()):
        builder.append(f"{d}:{f}")
    return "|".join(builder)


pows = set()
n = 1
while n <= 1e9:
    nstr = str(n)
    pows.add(key(nstr))
    n <<= 1


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return key(str(n)) in pows
