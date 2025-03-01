# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        cur_max = 0

        while l <= r and r < len(s):
            if not s[r] in seen:
                seen[s[r]] = True
                r += 1
                cur_max = max(cur_max, r - l)
                continue

            while s[r] in seen:
                del seen[s[l]]
                l += 1

        return cur_max
