from collections import Counter
from typing import List


# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Case 1 - two different letters:
        # - must require 2 mirror version to form palindrome (append to both end of the palindrome)
        # Case 2 - two same letters:
        # - can be the center of a palindrome

        cnt = Counter(words)

        found_center = False
        length = 0
        for w, f in cnt.items():
            if w[0] == w[1]:  # same
                if f % 2 == 1:
                    found_center = True
                length += (f - (f % 2)) * 2
                continue

            rev = w[1] + w[0]
            length += min(cnt[w], cnt[rev]) * 2 * 2
            cnt[w] = 0

        if found_center:
            length += 2

        return length
