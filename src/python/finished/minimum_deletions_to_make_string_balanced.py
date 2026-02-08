# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix_b = [0] * (n + 1)
        suffix_a = [0] * (n + 1)
        for i in range(n):
            prefix_b[i + 1] = prefix_b[i] + (1 if s[i] == "b" else 0)
            j = n - i - 1
            suffix_a[j] = suffix_a[j + 1] + (1 if s[j] == "a" else 0)

        return min(prefix_b[i] + suffix_a[i] for i in range(n + 1))
