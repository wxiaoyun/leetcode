# https://leetcode.com/problems/ipo/

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cpq = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(cpq)

        pq = []
        projects = 0
        cur_w = w

        while projects < k:
            while cpq:
                item = heapq.heappop(cpq)

                if item[0] <= cur_w:
                    heapq.heappush(pq, (-item[1]))
                else:
                    heapq.heappush(cpq, item)
                    break
            
            if not pq:
                break

            pft = heapq.heappop(pq)
            projects += 1
            cur_w += (-pft)
        
        return cur_w