import heapq

# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        visited = set()

        # Number of vertices: m * n
        # Number of edges: 3 * m * n
        # O(E log V) = O(mn log (mn))

        # (steps, i, j), where word1[:i] (after some operations) is equal to word2[:j]
        q = [(0, 0, 0)]
        while q:
            steps, i, j = heapq.heappop(q)
            if i >= len(word1) and j >= len(word2):
                return steps

            key = (i, j)
            if key in visited:
                continue
            visited.add(key)

            # deletion: we have excess characters
            if j >= len(word2):
                heapq.heappush(q, (steps + 1, i + 1, j))
                continue

            # insertion: we do not have sufficient characters
            if i >= len(word1):
                heapq.heappush(q, (steps + 1, i, j + 1))
                continue

            # no modification is needed
            if word1[i] == word2[j]:
                heapq.heappush(q, (steps, i + 1, j + 1))
                continue

            # deletion
            heapq.heappush(q, (steps + 1, i + 1, j))
            # insertion
            heapq.heappush(q, (steps + 1, i, j + 1))
            # replacement
            heapq.heappush(q, (steps + 1, i + 1, j + 1))

        return -1
