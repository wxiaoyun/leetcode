# https://leetcode.com/problems/task-scheduler/

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tabulation = {}

        max_freq = 0

        for t in tasks:
            if not t in tabulation:
                tabulation[t] = 0
            tabulation[t] += 1
            max_freq = max(max_freq, tabulation[t])

        count_max_freq = 0
        for v in tabulation.values():
            if v == max_freq:
                count_max_freq += 1
        
        result = (max_freq - 1) * (n + 1) + count_max_freq
        return max(result, len(tasks))
        