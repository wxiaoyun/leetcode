import heapq
from typing import List


# TLE
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        events = [[] for _ in range(len(nums))]
        for l, r, k, v in queries:
            events[l].append((r, k, v))

        MOD = int(1e9) + 7
        ans = 0
        for i, n in enumerate(nums):
            cur = n
            for r, k, v in events[i]:
                cur = (cur * v) % MOD
                if i + k <= r:
                    events[i + k].append((r, k, v))

            ans ^= cur
            events[i] = None

        return ans


# TLE
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        event_queue = [(l, r, k, v) for l, r, k, v in queries]
        heapq.heapify(event_queue)

        MOD = int(1e9) + 7
        ans = 0
        for i, n in enumerate(nums):
            cur = n
            while event_queue:
                l, r, k, v = event_queue[0]
                if r < i:
                    heapq.heappop(event_queue)
                    continue

                if l != i:
                    break

                heapq.heappop(event_queue)
                cur = (cur * v) % MOD
                heapq.heappush(event_queue, (l + k, r, k, v))

            ans ^= cur

        return ans
