import heapq

# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers


class Solution:
    def minimumDistance(self, word: str) -> int:
        grid = [
            "abcdef".upper(),
            "ghijkl".upper(),
            "mnopqr".upper(),
            "stuvwx".upper(),
            "yz".upper(),
        ]
        alpha_index = {}
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                alpha_index[ch] = (i, j)

        DIST = 0
        NEXT_INDEX = 0
        HAND_ONE_INDEX = -1
        HAND_TWO_INDEX = -1
        pq = [(DIST, NEXT_INDEX, HAND_ONE_INDEX, HAND_TWO_INDEX)]
        visited = set()
        while pq:
            dist, nx, i1, i2 = heapq.heappop(pq)
            node = (nx, i1, i2)
            if node in visited:
                continue
            visited.add(node)

            if nx >= len(word):
                return dist

            next_ch = word[nx]
            next_i, next_j = alpha_index[next_ch]

            # use hand 1
            move_hand_one_dist = 0
            if i1 >= 0:
                h1_i, h1_j = alpha_index[word[i1]]
                move_hand_one_dist = abs(h1_i - next_i) + abs(h1_j - next_j)
            heapq.heappush(pq, (dist + move_hand_one_dist, nx + 1, nx, i2))

            # use hand 2
            move_hand_two_dist = 0
            if i2 >= 0:
                h2_i, h2_j = alpha_index[word[i2]]
                move_hand_two_dist = abs(h2_i - next_i) + abs(h2_j - next_j)
            heapq.heappush(pq, (dist + move_hand_two_dist, nx + 1, i1, nx))

        return -1
