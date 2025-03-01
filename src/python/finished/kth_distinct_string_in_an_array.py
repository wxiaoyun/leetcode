# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from typing import Dict, List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seem: Dict[int, int] = {}

        for i in range(len(arr)):
            s = arr[i]

            if s not in seem:
                seem[s] = i
                continue

            if seem[s] < 0:
                continue

            seem[s] = -1  # second time we see s

        # distinct = [itm for itm in seem.items()]
        # distinct = filter(lambda x: x[1] >= 0, distinct)
        # distinct = sorted(distinct, key=lambda x: x[1])
        # return distinct[k-1][0] if k <= len(distinct) else ""

        for s in arr:
            if seem[s] >= 0:
                k -= 1

            if k == 0:
                return s
        return ""
