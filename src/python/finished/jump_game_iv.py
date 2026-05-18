from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/jump-game-iv


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        lookup = defaultdict(list)
        for i, v in enumerate(arr):
            lookup[v].append(i)

        visited = [False] * n
        s = 0
        q = deque([0])
        while q:
            l = len(q)
            for _ in range(l):
                i = q.popleft()

                if i == n - 1:
                    return s

                adj_list = [i - 1, i + 1]
                for j in lookup[arr[i]]:
                    if not visited[j] and j not in [i, i - 1, i + 1]:
                        adj_list.append(j)

                for j in adj_list:
                    if j < 0 or j >= n or visited[j]:
                        continue
                    q.append(j)
                    visited[j] = True

                del lookup[arr[i]]

            s += 1

        return -1
