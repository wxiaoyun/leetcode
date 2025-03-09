from typing import List

# https://leetcode.com/problems/alternating-groups-ii/description


# O(n) time
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        count = 0

        l = 0
        prev = None
        for r in range(N + k - 1):
            rr = r % N

            if colors[rr] == prev:
                l = r
            prev = colors[rr]

            if r - l + 1 == k:
                count += 1
                l += 1

        return count


# O(n^2) time
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        count = 0

        for i in range(N):
            cur = None
            is_alt = True
            for j in range(k):
                idx = (i + j) % N
                if cur == colors[idx]:
                    is_alt = False
                    break

                cur = colors[idx]

            if is_alt:
                count += 1

        return count
