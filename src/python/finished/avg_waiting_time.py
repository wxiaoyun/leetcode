# https://leetcode.com/problems/average-waiting-time

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = [None] * len(customers)

        avail = 0
        for i, (arrival, time) in enumerate(customers):
            start_time = max(avail, arrival)
            finish_time = time + start_time
            wait[i] = finish_time-arrival
            avail = finish_time
   
        return sum(wait) / len(wait)
