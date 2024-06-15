# https://leetcode.com/problems/height-checker/

import copy
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = copy.deepcopy(heights)
        expected.sort()

        cnt = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                cnt+=1
        return cnt
