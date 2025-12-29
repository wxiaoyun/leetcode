from collections import deque
from typing import List

# https://leetcode.com/problems/time-needed-to-buy-tickets


# O(n)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        min_rounds = tickets[k]

        t = 0
        for i, tkt in enumerate(tickets):
            max_tkt = min(tkt, min_rounds)
            if i > k:
                max_tkt = min(tkt, min_rounds - 1)

            t += max_tkt
        return t


# O(n * max(tickets))
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tq = deque((t, i) for i, t in enumerate(tickets))

        t = 0
        while True:
            t_rem, i = tq.popleft()
            t += 1

            if t_rem - 1 == 0:
                if i == k:
                    return t
                continue

            tq.append((t_rem - 1, i))

        return -1
