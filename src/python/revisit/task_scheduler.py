import heapq
from collections import Counter
from typing import List

# https://leetcode.com/problems/task-scheduler/


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        pq = [(-c, 0, task) for task, c in cnt.items()]
        heapq.heapify(pq)

        t = 0
        while pq:
            next_rd = []
            for i in range(n + 1):
                if not pq:
                    break

                rem_cnt, start_time, task = heapq.heappop(pq)
                if rem_cnt == 0:
                    continue
                t = max(t, start_time)
                t += 1

                next_rd.append((rem_cnt + 1, t + n, task))

            for item in next_rd:
                heapq.heappush(pq, item)

        return t


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
