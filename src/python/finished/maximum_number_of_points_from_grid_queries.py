from typing import List
import heapq

# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        R = len(grid)
        C = len(grid[0])

        cache_key = []
        cache_count = []

        cur_total = 0
        visited = set()
        start_val = grid[0][0]
        pq = [(start_val, 0, 0)]
        while pq:
            cur_val, _, _ = pq[0]

            while pq and pq[0][0] <= cur_val:
                # only pop if value is less than or equal to cur_val
                _, i, j = heapq.heappop(pq)
                n = (i, j)
                if n in visited:
                    continue
                visited.add(n)
                cur_total += 1

                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if min(ii, jj) < 0 or ii >= R or jj >= C:
                        continue
                    if (ii, jj) in visited:
                        continue
                    heapq.heappush(pq, (grid[ii][jj], ii, jj))

            cache_key.append(cur_val)
            cache_count.append(cur_total)

        res = []

        def find(value: int) -> int:
            if value <= start_val:
                return 0

            # binary search to find left bound value
            l, r = 0, len(cache_key)
            while l < r:
                m = l + (r - l) // 2

                if cache_key[m] < value:
                    l = m + 1
                else:
                    r = m

            return cache_count[l - 1]

        return [find(q) for q in queries]
