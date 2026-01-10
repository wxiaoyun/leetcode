# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def compute(dp: dict, s1: str, s2: str, i: int, j: int) -> int:
            key = (i, j)
            if key in dp:
                return dp[key]

            if i >= len(s1) or j >= len(s2):
                left_sum = sum(ord(c) for c in s1[i:]) if i < len(s1) else 0
                right_sum = sum(ord(c) for c in s2[j:]) if j < len(s2) else 0
                total = left_sum + right_sum
                dp[key] = total
                return total

            INF = 1 << 31
            best = INF
            c1, c2 = s1[i], s2[j]

            if c1 == c2:
                best = min(best, compute(dp, s1, s2, i + 1, j + 1))
            else:
                best = min(
                    best,
                    ord(c1) + compute(dp, s1, s2, i + 1, j),
                    ord(c2) + compute(dp, s1, s2, i, j + 1),
                )

            dp[key] = best
            return best

        return compute({}, s1, s2, 0, 0)
