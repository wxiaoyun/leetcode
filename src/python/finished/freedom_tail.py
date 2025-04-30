# https://leetcode.com/problems/freedom-trail


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # What is the minimum number of steps to key in the remaining keys given ring position
        # Let S(d, i, dir) = rotation steps required to reach letter `d` from ring index `p` given direction `dir`

        # T(p, i) = min(
        #   S(key[i], p, left) + T(p_next_left, i + 1),
        #   S(key[i], p, right) + T(p_next_right, i + 1),
        # ) + 1
        #
        # T(p, len(key)) = 0

        N = len(key)
        R = len(ring)
        dp = {}  # Dict<Tuple[ring_pos, key_pos], int>

        def compute(p: int, i: int) -> int:
            if i == N:
                return 0

            k = (p, i)
            if k in dp:
                return dp[k]

            char = key[i]
            left_dist = find_next(char, p, -1)
            right_dist = find_next(char, p, 1)

            best = (
                min(
                    left_dist + compute((p - left_dist) % R, i + 1),
                    right_dist + compute((p + right_dist) % R, i + 1),
                )
                + 1
            )

            dp[k] = best
            return best

        def find_next(target: str, pos: int, dir: int) -> int:
            dist = 0
            p = pos
            while ring[p % R] != target:
                p += dir
                dist += 1
            return dist

        return compute(0, 0)
