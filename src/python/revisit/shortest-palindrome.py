# https://leetcode.com/problems/shortest-palindrome/


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        rev = s[::-1]

        for i in range(N):
            if s[: N - i] == rev[i:]:
                return rev[:i] + s
        return ""
