from typing import List

# https://leetcode.com/problems/jump-game-iii


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n

        stk = [start]
        while stk:
            i = stk.pop()
            if i < 0 or i >= n or visited[i]:
                continue
            visited[i] = True

            if arr[i] == 0:
                return True

            stk.append(i + arr[i])
            stk.append(i - arr[i])

        return False
