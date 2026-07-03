import heapq
from typing import List

# https://leetcode.com/problems/network-recovery-pathways


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        adj_list = [[] for _ in range(n)]
        for u, v, c in edges:
            if online[v]:
                adj_list[u].append((v, c))

        def possible(min_rec: int) -> bool:
            pq = [(0, 0, 0)]
            visited = set()
            while pq:
                neg_min_rec, total_rec, node = heapq.heappop(pq)
                # print(neg_min_rec, total_rec, node)
                if total_rec > k:
                    return False
                if node in visited:
                    continue
                visited.add(node)
                if node == n - 1:
                    return True

                for v, cc in adj_list[node]:
                    if cc < min_rec:
                        continue
                    if v in visited:
                        continue
                    heapq.heappush(pq, (-min(-neg_min_rec, cc), total_rec + cc, v))

            return False

        l, r = 0, max((c for _, _, c in edges), default=0) + 1
        ans = -1
        while l < r:
            m = l + (r - l) // 2
            if possible(m):
                ans = m
                l = m + 1
            else:
                r = m
        return ans
