# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        moves = s
        best = -1
        n, s, e, w = 0, 0, 0, 0
        for d in moves:
            match d:
                case "N":
                    n += 1
                case "S":
                    s += 1
                case "E":
                    e += 1
                case "W":
                    w += 1
            max_delta = min(k, min(n, s, k) + min(e, w, k))
            best = max(best, abs(n - s) + abs(e - w) + 2 * max_delta)

        return best
