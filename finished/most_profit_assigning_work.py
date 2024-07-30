# https://leetcode.com/problems/most-profit-assigning-work/

import heapq
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()

        # min heap, extract tasks with lowest difficulty
        tpq = [(difficulty[i], profit[i]) for i in range(len(profit))]
        heapq.heapify(tpq)

        cur_best_profit = 0
        total_profit = 0

        for max_ability in worker:
            while tpq and tpq[0][0] <= max_ability:
                _, p = heapq.heappop(tpq)
                cur_best_profit = max(cur_best_profit, p)
            
            total_profit += cur_best_profit
        
        return total_profit
            
