# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        cur_freq = 0
        cur_sum = 0
        for freq in cnt.values():
            if freq < cur_freq:
                continue
            if freq > cur_freq:
                cur_freq = freq
                cur_sum = freq
                continue
            cur_sum += freq

        return cur_sum
