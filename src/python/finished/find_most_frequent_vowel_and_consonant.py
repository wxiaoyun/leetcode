# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_freq = defaultdict(int)
        cosnt_freq = defaultdict(int)
        vowels = set(list("aeiuo"))

        for ch in s:
            if ch in vowels:
                vowel_freq[ch] += 1
            else:
                cosnt_freq[ch] += 1

        vowel_freq[""] = 0
        cosnt_freq[""] = 0
        return max(vowel_freq.values()) + max(cosnt_freq.values())
