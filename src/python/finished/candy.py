from collections import deque
from typing import List

# https://leetcode.com/problems/candy


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        # topological sort
        adj_list = [[] for _ in range(N)]
        in_deg = [0] * N
        for n in range(N):
            prev = n - 1
            if prev >= 0 and ratings[prev] > ratings[n]:
                in_deg[prev] += 1
                adj_list[n].append(prev)

            next = n + 1
            if next < N and ratings[next] > ratings[n]:
                in_deg[next] += 1
                adj_list[n].append(next)

        candies = [1] * N
        noptr = deque([])
        for i, f in enumerate(in_deg):
            if f == 0:
                noptr.append(i)

        while noptr:
            n = noptr.popleft()

            if n - 1 >= 0:
                c = candies[n - 1]
                if ratings[n - 1] < ratings[n]:
                    c += 1
                candies[n] = max(candies[n], c)

            if n + 1 < N:
                c = candies[n + 1]
                if ratings[n + 1] < ratings[n]:
                    c += 1
                candies[n] = max(candies[n], c)

            for nb in adj_list[n]:
                in_deg[nb] -= 1
                if in_deg[nb] == 0:
                    noptr.append(nb)

        return sum(candies)
