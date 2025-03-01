# https://leetcode.com/problems/number-of-senior-citizens

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([None for d in details if int(d[11:13]) > 60])