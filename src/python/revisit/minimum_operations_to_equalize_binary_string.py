import heapq

# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/


# TLE: O(nklogn)
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zeros = s.count("0")
        pq = [(zeros, 0)]
        visited = set()
        while pq:
            z, steps = heapq.heappop(pq)
            if z in visited:
                continue
            visited.add(z)

            if z == 0:
                return steps

            for i in range(max(0, k + z - len(s) - 1), min(z, k)):
                rm = i + 1
                add = k - rm
                heapq.heappush(pq, (z - rm + add, steps + 1))

        return -1
