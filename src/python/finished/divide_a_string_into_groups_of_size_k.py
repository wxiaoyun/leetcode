from typing import List

# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []
        for i in range(0, len(s), k):
            groups.append(s[i : i + k])
        if len(groups[-1]) != k:
            groups[-1] = groups[-1] + (fill * (k - len(groups[-1])))
        return groups
